from DarkMatterMaytok.settings import USER_RANK


def user_has_min_rank(user, rank):
    flat_ranks = [i[0] for i in USER_RANK]
    new_ranks = flat_ranks.copy()
    for i in range(len(flat_ranks)):
        if rank != new_ranks[0]:
            new_ranks.pop(0)
        else:
            break
    return user.rank in new_ranks
