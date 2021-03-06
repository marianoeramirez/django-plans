from django.core.management import BaseCommand

from plans.models import CustomerPlan


class Command(BaseCommand):
    help = 'Creates UserPlans for all Users'

    def handle(self, *args, **options):  # pragma: no cover
        userplans = CustomerPlan.create_for_customers_without_plan()
        self.stdout.write("%s user plans was created" % userplans.count())
