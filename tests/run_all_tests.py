#!/usr/bin/env python3

import pytest
import sys
import os
from pathlib import Path

class TestRunner:
    def __init__(self):
        self.tests_dir = Path(__file__).parent
        
    def run_all_tests(self):
        """Запуск всех тестов"""
        print(" Запускаем ВСЕ тесты...")
        return self._run_pytest([str(self.tests_dir)])
    
    def run_health_tests(self):
        """Запуск только health тестов"""
        print("Запускаем health тесты...")
        return self._run_pytest([str(self.tests_dir / "test_health.py")])
    
    def run_shock_tests(self):
        """Запуск только shock тестов"""
        print("Запускаем shock тесты...")
        return self._run_pytest([str(self.tests_dir / "test_shock_check.py")])
    
    def run_auth_tests(self):
        """Запуск только auth тестов"""
        print("Запускаем auth тесты...")
        return self._run_pytest([str(self.tests_dir / "test_auth.py")])
    
    def run_name_tests(self):
        """Запуск только name тестов"""
        print("Запускаем name тесты...")
        return self._run_pytest([str(self.tests_dir / "test_user_name.py")])
    
    def _run_pytest(self, test_paths):
        """Внутренний метод для запуска pytest"""
        args = test_paths + ["-v", "--tb=short"]
        return pytest.main(args)
    
    def interactive_menu(self):
        """Интерактивное меню для выбора тестов"""
        while True:
            print("\n" + "=" * 50)
            print("МЕНЮ ЗАПУСКА ТЕСТОВ")
            print("=" * 50)
            print("1. Запустить ВСЕ тесты")
            print("2. Health тесты")
            print("3. Shock тесты (ШОКовость)")
            print("4. Auth тесты (авторизация)")
            print("5. Name тесты (изменение имени)")
            print("0. Выход")
            print("=" * 50)
            
            choice = input("Выберите опцию (0-5): ").strip()
            
            if choice == "0":
                print("До свидания!")
                break
            elif choice == "1":
                self.run_all_tests()
            elif choice == "2":
                self.run_health_tests()
            elif choice == "3":
                self.run_shock_tests()
            elif choice == "4":
                self.run_auth_tests()
            elif choice == "5":
                self.run_name_tests()
            else:
                print("Попробуйте снова.")
            
            input("\nНажмите Enter для продолжения...")


def main():
    """Главная функция"""
    runner = TestRunner()
    
    # Если есть аргументы командной строки, запускаем без меню
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            return runner.run_all_tests()
        elif sys.argv[1] == "health":
            return runner.run_health_tests()
        elif sys.argv[1] == "shock":
            return runner.run_shock_tests()
        elif sys.argv[1] == "auth":
            return runner.run_auth_tests()
        elif sys.argv[1] == "name":
            return runner.run_name_tests()
        else:
            print(f"Неизвестный аргумент: {sys.argv[1]}")
            print("Доступные: all, health, shock, auth, name")
            return 1
    else:
        # Интерактивное меню
        runner.interactive_menu()
        return 0


if __name__ == "__main__":
    sys.exit(main())