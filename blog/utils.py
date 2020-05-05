from django.contrib.auth.decorators import user_passes_test

from DarkMatterMaytok.settings import USER_RANK


def require_mini_rank(rank, login_url=None):
    """
    Checks if the user has a minimum rank to access the page
    """

    def has_rank(user):
        flat_ranks = [i[0] for i in USER_RANK]
        new_ranks = flat_ranks.copy()
        for i in range(len(flat_ranks)):
            if rank != new_ranks[0]:
                new_ranks.pop(0)
            else:
                break
        return user.rank in new_ranks

    return user_passes_test(has_rank, login_url=login_url)
