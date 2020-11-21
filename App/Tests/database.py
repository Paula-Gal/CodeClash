from App.Database import db, User, Problem, ProblemTest


def populate_database():
    db.session.add(User('test@gmail.com', '1234', 'claudiu', 'neamtu'))
    db.session.add(User('cum_sa_te_cheme_bogdana@gmail.com', 'mirel', 'B', 'M'))

    db.session.commit()

    problem = Problem(name='Problema ffff grea', description='adunare', difficulty=1)

    db.session.add(problem)
    db.session.commit()

    db.session.add(
        ProblemTest(
            problem_id=problem.id,
            input_data='1 2',
            output_data='3',
            max_execution_time=1,
            max_memory_size=50*1000,
            points=1
        )
    )

    db.session.add(
        ProblemTest(
            problem_id=problem.id,
            input_data='1 2 3',
            output_data='6',
            max_execution_time=1,
            max_memory_size=50 * 1000,
            points=2
        )
    )

    db.session.add(
        ProblemTest(
            problem_id=problem.id,
            input_data='5 5 5 5 5',
            output_data='25',
            max_execution_time=1,
            max_memory_size=50 * 1000,
            points=7
        )
    )

    db.session.commit()
