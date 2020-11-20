from App.Database import db, User, Problem


def populate_database():
    db.session.add(User('playercoco2014@gmail.com', '12345678', 'claudiu', 'neamtu'))
    db.session.add(User('cum_sa_te_cheme_bogdana@gmail.com', 'mirel', 'B', 'M'))

    db.session.commit()

    db.session.add(Problem(name='Problema ffff grea', description='adunare', difficulty='HIGH'))
