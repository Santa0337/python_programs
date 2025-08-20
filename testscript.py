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
        self.parent.parameters.update(ios1=ios1, ios2=ios2)

        # get links between devices
        links = ios1.find_links(ios2)
        assert len(links) >= 1, 'require one link between ios1 and ios2'

    @aetest.subsection
    def establish_connections(self, steps, ios1, ios2):
        with steps.start(f'Connecting to {ios1.name}'):
            ios1.connect()
        with steps.start(f'Connecting to {ios2.name}'):
            ios2.connect()

@aetest.loop(device=('R1', 'R2'))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination=('10.10.20.171', '10.10.20.172'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination)
        except Exception as e:
            self.failed(
                f'Ping to {destination} from device {device} failed: {str(e)}',
                goto=['exit']
            )
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            if match:
                success_rate = match.group('rate')
                logger.info(f'Ping {destination} success rate: {success_rate}%')
            else:
                logger.warning(f'Ping output not matched: {result}')

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, ios1, ios2):
        with steps.start(f'Disconnecting from {ios1.name}'):
            ios1.disconnect()
        with steps.start(f'Disconnecting from {ios2.name}'):
            ios2.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
