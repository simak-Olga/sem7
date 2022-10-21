
import view
import rational
import logger
import complex


match view.item_sel():
    case 0:
        expr = view.get_expr()
        expr = expr.replace(" ", "")
        if expr.find("j") < 0:
            res = rational.parse_all(expr)
        else:
            res = complex.re_parse(expr)
        logger.write(f"Результат вычисления: {expr} = {res}")
        view.show(f"Результат вычисления: {expr} = {res}")
    case 1:
        view.show(logger.read_all())
    case 2:
        view.show("Логи очищены!") if logger.clear(
        ) else view.show("Логов нет!")