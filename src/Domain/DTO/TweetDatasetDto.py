from datetime import datetime


class TweetDatasetDto:

    def __init__(self, updated_at: datetime, new_records: int, all_records: int, ):
        self.updated_at = updated_at.isoformat()
        self.new_records = new_records
        self.all_records = all_records
