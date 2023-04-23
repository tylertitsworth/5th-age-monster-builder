class Ability:
    def __init__(self,
        dc=None,
        description=None,
        name=None
    ):
        self.name = name

class Attack:
    def __init__(self,
        defense=None,
        effect=None,
        hit_effect=None,
        name=None,
        range=None,
        triggers=[],
        type=None
    ):
        self.name = name

class Creature:
    def __init__(self, 
        abilities=[],
        attacks=[],
        condition_immunities=[],
        favored_defenses=[],
        immunities=[],
        initiative_type=None,
        level=None,
        name=None,
        role=None,
        size=None,
        strength=None,
        template=None,
        type=None,
        vulnerabilities=[]
    ):
        self.name = name

class Trigger:
    def __init__(self,
        dc=None,
        parity=None,
        recharge=None
    ):
        pass
