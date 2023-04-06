from .BaseClient import BaseClient
import re


class TimeClient(BaseClient):
    base_url = 'https://worldtimeapi.org/api/timezone/'

    def get_time(self, timezone='Europe/London') -> str:
        print(f'[client.time] getting time for timezone {timezone}')
        response = self.do_request(timezone)
        full_date_time = response['datetime']
        _, current_time, _, _, _ = self.__extract_time_data(full_date_time)
        return current_time

    @staticmethod
    def __extract_time_data(full_date_time) -> (int, int, int, int, int):
        matched_time = re.match(r"^(\d+-\d+-\d+)T(\d+:\d+):(\d+)\.(\d+)([-+]\d+:\d+)$", full_date_time)
        current_date = matched_time.group(1)
        current_time = matched_time.group(2)
        current_seconds = matched_time.group(3)
        current_milliseconds = matched_time.group(4)
        current_offset = matched_time.group(5)

        return current_date, current_time, current_seconds, current_milliseconds, current_offset