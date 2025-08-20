
from pyats import aetest
import re
import logging
logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self, testbed, ios1_name='R1', ios2_name='R2'):
        ios1 = testbed.devices[ios1_name]
        ios2 = testbed.devices[ios2_name]

        # add to testscript parameters
        self.parent.parameters.update(R1=ios1, R2=ios2)

        # get links between devices
        links = ios1.find_links(ios2)
        assert len(links) >= 1, 'require one link between ios1 and ios2'

    @aetest.subsection
    def establish_connections(self, steps, R1, R2):
        with steps.start(f'Connecting to {R1.name}'):
            R1.connect()
        with steps.start(f'Connecting to {R2.name}'):
            R2.connect()

@aetest.loop(device=('R1', 'R2'))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination=('10.10.20.171', '10.10.20.172'))
    def ping(self, device, destination):
        vrf = 'Mgmt-intf'   # <-- change to your actual VRF name if different
        device_obj = self.parameters[device]

        # Skip self-ping if desired (optional)
        if (device == 'R1' and destination == '10.10.20.171') or \
           (device == 'R2' and destination == '10.10.20.172'):
            self.skipped(f"{device} skipping self-ping")
            return

        # Use VRF-aware ping if address is VRF-bound
        try:
            if destination.startswith("10.10.20."):
                cmd = f'ping vrf {vrf} {destination}'
                result = device_obj.execute(cmd)
            else:
                result = device_obj.ping(destination)
        except Exception as e:
            self.failed(
                f'Ping to {destination} from device {device} failed: {str(e)}',
                goto=['exit']
            )
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            if match:
                success_rate = match.group('rate')
                logger.info(f'Ping {destination} from {device} success rate: {success_rate}%')
                if int(success_rate) < 100:
                    self.failed(f'Ping to {destination} from device {device} SUCCESS RATE < 100%')
            else:
                logger.warning(f'Ping output not matched: {result}')


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, R1, R2):
        with steps.start(f'Disconnecting from {R1.name}'):
            R1.disconnect()
        with steps.start(f'Disconnecting from {R2.name}'):
            R2.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
