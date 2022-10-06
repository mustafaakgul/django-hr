# from django.db import models
#
#
# class Jobs(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
#     case_name = models.CharField(max_length=50)
#     currency_type = models.CharField(max_length=50, choices=CASE_TYPE, default=CASE_TYPE[0][0])
#     initial_balance = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True, default=0)
#     case_date = models.DateTimeField(default=timezone.now)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class CaseCommon(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
#     case_name = models.CharField(max_length=50)
#     currency_type = models.CharField(max_length=50, choices=CASE_TYPE, default=CASE_TYPE[0][0])
#     initial_balance = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True, default=0)
#     case_date = models.DateTimeField(default=timezone.now)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class Case(CaseCommon):
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class CaseDeleted(CaseCommon):
#     old_model_created_date = models.DateTimeField(blank=True, null=True)
#     old_model_update_date = models.DateTimeField(blank=True, null=True)
#
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class CaseArchieved(CaseCommon):
#     old_model_created_date = models.DateTimeField(blank=True, null=True)
#     old_model_update_date = models.DateTimeField(blank=True, null=True)
#
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name