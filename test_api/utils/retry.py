import time
import logging
from functools import wraps
from typing import Callable, Type, Tuple, Optional

logger = logging.getLogger(__name__)

# Декоратор для повторных попыток выполнения функции при ошибках
# Используется для устойчивости к временным сбоям сети/сервера
def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    on_retry: Optional[Callable] = None
):
    """
    Декоратор для повторных попыток выполнения функции
    
    :param max_attempts: максимальное количество попыток
    :param delay: задержка между попытками в секундах
    :param exceptions: кортеж исключений, при которых нужно повторять попытку
    :param on_retry: функция, вызываемая при каждой повторной попытке
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:  # если это не последняя попытка
                        logger.warning(
                            f"Попытка {attempt + 1} из {max_attempts} не удалась: {str(e)}. "
                            f"Повторная попытка через {delay} сек..."
                        )
                        if on_retry:
                            on_retry(attempt + 1, e)
                        time.sleep(delay)
                    else:
                        logger.error(
                            f"Все {max_attempts} попыток не удались. "
                            f"Последняя ошибка: {str(e)}"
                        )
            
            raise last_exception  # пробрасываем последнее исключение
            
        return wrapper
    return decorator 