def get_user_rank_name(user):
    if user.rank == 'B' and user.gender == 'M':
        return 'Barón'
    if user.rank == 'C' and user.gender == 'M':
        return 'Conde'
    if user.rank == 'D' and user.gender == 'M':
        return 'Duque'
    if user.rank == 'K' and user.gender == 'M':
        return 'Rey'
    if user.rank == 'E' and user.gender == 'M':
        return 'Emperador'
    if user.rank == 'B' and user.gender == 'F':
        return 'Baronesa'
    if user.rank == 'C' and user.gender == 'F':
        return 'Condesa'
    if user.rank == 'D' and user.gender == 'F':
        return 'Duquesa'
    if user.rank == 'K' and user.gender == 'F':
        return 'Reina'
    if user.rank == 'E' and user.gender == 'F':
        return 'Emperatriz'
    return ''
