from src.repos.redis.user import u
from src.repos.postgres.user import UserRepository
from src.constants.state import State
from logging import getLogger

logger = getLogger(__name__)


async def users_on_startup():
    """Manage states for saved users and remove unavailable users from cache"""

    cached_users_ids = [user.split(":")[1] for user in await u.get_users()]
    saved_users = await UserRepository.list()
    saved_users_ids = [str(user.id) for user in saved_users]

    # remove from cache deleted users
    for cached_user_id in cached_users_ids:
        if cached_user_id not in saved_users_ids:
            await u.delete(pk=cached_user_id)
            logger.info(f"User {cached_user_id} was removed from cache")

    # set states for saved users
    for saved_user_id in saved_users_ids:
        if saved_user_id not in cached_users_ids:
            await u.set_state(user_id=saved_user_id, state=State.WAIT)
            logger.info(f"User {saved_user_id} was added to cache and set state to {State.WAIT}")
