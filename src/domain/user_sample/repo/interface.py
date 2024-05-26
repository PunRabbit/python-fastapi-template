from abc import ABCMeta, abstractmethod

from domain.user_sample.repo.basemodel import UserInsertInfo, UserWaitInfo, UserBaseInfo


class UserSampleRepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert_user(self, user_info: UserInsertInfo) -> bool:
        pass

    @abstractmethod
    def find_user(self, user_id: str) -> UserBaseInfo:
        pass

    @abstractmethod
    def insert_wait_list(self, user_wait_info: UserWaitInfo) -> bool:
        pass

    @abstractmethod
    def find_wait_list(self, user_id: str) -> UserWaitInfo:
        pass

    @abstractmethod
    def delete_wait_list(self, user_id: str) -> UserWaitInfo:
        pass
