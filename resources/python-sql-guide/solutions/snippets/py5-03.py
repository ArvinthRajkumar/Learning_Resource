import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("shop.orders")
log.debug("not shown at INFO level")
log.info("order %s created", 42)          # lazy %-style formatting
log.warning("stock low for %s", "pen")
try:
    1 / 0
except ZeroDivisionError as exc:
    log.error("failed to compute: %s", exc)   # log.exception(...) would also include the traceback
