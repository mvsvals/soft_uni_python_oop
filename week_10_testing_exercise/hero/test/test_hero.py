from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.dummy_hero = Hero('testuser', 99, 2000.00, 500.00)
        self.enemy_hero = Hero('testenemy', 55, 1000.00, 200.00)

    def test_hero_class_attributes(self):
        self.assertIsInstance(self.dummy_hero.username, str)
        self.assertIsInstance(self.dummy_hero.level, int)
        self.assertIsInstance(self.dummy_hero.health, float)
        self.assertIsInstance(self.dummy_hero.damage, float)

    def test_hero_class_init(self):
        self.assertEqual('testuser', self.dummy_hero.username)
        self.assertEqual(99, self.dummy_hero.level)
        self.assertEqual(2000, self.dummy_hero.health)
        self.assertEqual(500, self.dummy_hero.damage)

    def test_hero_battle_self_raises(self):
        with self.assertRaises(Exception) as e:
            self.dummy_hero.battle(self.dummy_hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_hero_battle_hero_with_zero_or_negative_health_raises(self):
        self.assertEqual(99, self.dummy_hero.level)
        self.assertEqual(500, self.dummy_hero.damage)

        self.dummy_hero.health = 0
        with self.assertRaises(ValueError) as e:
            self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))


        self.dummy_hero.health = -20
        with self.assertRaises(ValueError) as e:
            self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))


    def test_hero_battle_enemy_hero_with_zero_or_negative_health_raises(self):
        self.assertEqual(55, self.enemy_hero.level)
        self.assertEqual(200, self.enemy_hero.damage)

        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as e:
            self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight testenemy. He needs to rest", str(e.exception))


        self.enemy_hero.health = -20
        with self.assertRaises(ValueError) as e:
            self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight testenemy. He needs to rest", str(e.exception))


    def test_hero_battle_draw(self):
        self.dummy_hero.health = 1
        self.enemy_hero.health = 1
        result = self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)
        self.assertEqual(-10999.0, self.dummy_hero.health)
        self.assertEqual(-49499.0, self.enemy_hero.health)

    def test_hero_battle_hero_win(self):
        self.dummy_hero.damage = 99999
        self.enemy_hero.damage = 1
        result = self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual('You win', result)
        self.assertEqual(1950, self.dummy_hero.health)
        self.assertEqual(100004, self.dummy_hero.damage)
        self.assertEqual(-9898901.0, self.enemy_hero.health)

    def test_hero_battle_enemy_win(self):
        self.dummy_hero.damage = 1
        self.enemy_hero.damage = 99999
        self.assertEqual(99, self.dummy_hero.level)
        result = self.dummy_hero.battle(self.enemy_hero)
        self.assertEqual('You lose', result)
        self.assertEqual(-5497945.0, self.dummy_hero.health)
        self.assertEqual(56, self.enemy_hero.level)
        self.assertEqual(906, self.enemy_hero.health)
        self.assertEqual(100004, self.enemy_hero.damage)


    def test_hero_str(self):
        result = str(self.dummy_hero)
        expected = f"Hero testuser: 99 lvl\n" + f"Health: 2000.0\n" + f"Damage: 500.0\n"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()