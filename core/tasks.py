from celery import shared_task

@shared_task
def notify_low_stock(product_id, product_name, current_quantity):
      print(
            f"📦 Notification: Product '{product_name}' (ID: {product_id}) "
            f"is low on stock ({current_quantity} remaining)."
      )
