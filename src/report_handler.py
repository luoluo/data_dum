#encoding: utf-8
from logger import Logger
from report_reader import report_reader
class report_handler:
    def __init__(self, logger):
        self.logger = logger
        self.useful_info = {}
        self.useful_time_info = {}
#   0           1         2         3              4            5        6             7                8               9         10          11              12           13         14
#time_period userid   username   website     register_time  audit_type status        audit_time      sent_time     is_illegal  illegal_type is_very_danger  register_time  is_new  l1_account
#time_period username l2_account l1_account  is_very_danger userid     register_time is_new          is_prism_found     9          10            11           12
#time_period username l1_account sources     is_very_danger userid     register_time is_new_register first_buy      sent_l2_audit l2_audit     audit_time  sent_time

#   0           1         2            3              4               5               6         7              8        9           10          11            12
#time_period userid   register_time first_buy  sent_audit2_time  deal_audit2_time  audit_time  sent_time  l1_account  audit_type  user_status  model_type  show_status

#        #    is_very_danger
#            if items[6] == u'是':
#                items[6] = 1
#            elif row != 1:
#                items[6] = 0
#
#        #    is_audit_by_prism
#            if items[7] == u'是':
#                items[7] = 1
#            elif row != 1:
#                items[7] = 0

    def get_useful_info(self, read_data):
        logger.info("dealing useful info")
        logger.info("dealing useful time info dealy time")
        for user_id in read_data.user_info_time_delay_map.keys():
            info_meta = [0]*13
            data_meta = read_data.user_info_time_delay_map[user_id]
            info_meta[0] = data_meta[0]
            info_meta[1] = data_meta[5]
            info_meta[2] = data_meta[6]
            info_meta[3] = data_meta[8]
            info_meta[4] = data_meta[9]
            info_meta[5] = data_meta[10]
            info_meta[6] = data_meta[11]
            info_meta[7] = data_meta[12]
            info_meta[8] = data_meta[2]
            user_stat = 0
            if data_meta[4] == u'是':
                user_stat += 0x2
            if data_meta[7] == u'是':
                user_stat += 0x4
            info_meta[10] = user_stat
            info_meta[9] = None
            info_meta[10] = None
            info_meta[11] = None
            info_meta[12] = None
            self.useful_time_info[user_id] = info_meta
            logger.debug(self.useful_time_info[user_id])
        logger.info("dealing useful time info dealy time end")

        logger.info("dealing useful info accurate")
        for user_id in read_data.user_info_accurate_map.keys():
            info_meta = [0]*13
            data_meta = read_data.user_info_accurate_map[user_id]
            if user_id in self.useful_info:
                self.useful_info[user_id][9] = data_meta[5]
            else :
                info_meta[0] = data_meta[0]
                info_meta[1] = data_meta[1]
                info_meta[2] = data_meta[4]
                info_meta[3] = None
                info_meta[4] = None
                info_meta[5] = None
                info_meta[6] = data_meta[7]
                info_meta[7] = data_meta[8]
                info_meta[8] = data_meta[14]
                user_stat = 0
                if data_meta[9] == u'是':
                    user_stat += 0x1
                if data_meta[11] == u'是':
                    user_stat += 0x2
                if data_meta[13] == u'是':
                    user_stat += 0x4
                info_meta[9] = None
                info_meta[10] = user_stat
                info_meta[11] = None
                info_meta[12] = None
                self.useful_info[user_id] = info_meta
                logger.debug(self.useful_info[user_id])
        logger.info("dealing useful info accurate end")

        logger.info("dealing useful info coverage")
        logger.info("coverage size = %d" % len(read_data.user_info_coverage_map.keys()))
        for user_id in read_data.user_info_coverage_map.keys():
            info_meta = [0]*13
            data_meta = read_data.user_info_coverage_map[user_id]
            if user_id in self.useful_info:
                pass
            else :
                info_meta[0] = data_meta[0]
                info_meta[1] = data_meta[5]
                info_meta[2] = data_meta[6]
                info_meta[3] = None
                info_meta[4] = None
                info_meta[5] = None
                info_meta[6] = None
                info_meta[7] = None
                info_meta[8] = data_meta[3]
                user_stat = 0
                if data_meta[7] == u'是':
                    user_stat += 0x4
                if data_meta[4] == u'是':
                    user_stat += 0x2
                info_meta[9] = None
                info_meta[10] = user_stat
                # found by prism
                if data_meta[8] == u'是':
                    info_meta[11] = 0x2
                else :
                    info_meta[11] = 0
                info_meta[12] = None
                self.useful_info[user_id] = info_meta
                logger.debug(self.useful_info[user_id])
        logger.info("dealing useful info coverage end")

        logger.info("the useful_time info as follows:")
        logger.debug("useful_time_info len = %d" % len(self.useful_time_info.keys()))
        logger.debug(self.useful_time_info.keys())
        for user_id in self.useful_time_info.keys():
            logger.debug(self.useful_time_info[user_id])

        logger.info("the useful info as follows:")
        logger.debug("useful_info len = %d" % len(self.useful_info.keys()))
        logger.debug(self.useful_info.keys())
        for user_id in self.useful_info.keys():
            logger.debug(self.useful_info[user_id])

        logger.info("dealing useful info end")

if __name__ == '__main__' :
    logger = Logger().get_logger()
    rr = report_reader(logger)
    data_input = "../data/test_all.xlsx"
    rr.dump_data(data_input)
    rh = report_handler(logger)
    rh.get_useful_info(rr)
