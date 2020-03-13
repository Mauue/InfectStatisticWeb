class ScheduleConfig:
    JOBS = [
            {
                'id': 'job3',
                'func': 'util.crawler:set_all_data_task',
                'args': '',
                'trigger': {
                    'type': 'interval',
                    'seconds': 21600  # 6个小时更新一次
                }
            },
        ]