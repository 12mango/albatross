from django.db import models

from albatross.utils.choices import EducationChoice, ClassificationChoice, SalaryTypeChoice, ResumeStatusChoice
from albatross.utils.models import SoftDeleteModel


class PostTree(models.Model):
    """
    岗位分类模型
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='岗位分类名')
    type = models.IntegerField(choices=ClassificationChoice.choices, verbose_name='岗位分类类型')
    father = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children', verbose_name='父级分类')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'recruits'
        db_table = 'tb_post_tree'
        verbose_name = '岗位分类'
        verbose_name_plural = verbose_name


class PostInfo(SoftDeleteModel):
    """
    岗位信息模型
    """

    pid = models.AutoField(primary_key=True, verbose_name='岗位ID')
    node_1 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='一级岗位',
                               related_name='node_1_related')  # 一级岗位
    node_2 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='二级岗位',
                               related_name='node_2_related')  # 二级岗位
    node_3 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='三级岗位',
                               related_name='node_3_related')  # 三级岗位
    post_name = models.CharField(max_length=100, default='', verbose_name='岗位名称')  # 岗位名称
    salary_min = models.IntegerField(default=0, verbose_name='薪资下限')
    salary_max = models.IntegerField(default=0, verbose_name='薪资上限')
    requirement = models.IntegerField(choices=EducationChoice.choices, default=EducationChoice.ALL, verbose_name='学历要求')  # 岗位学历要求
    experience = models.CharField(max_length=100, default='', verbose_name='工作经验')  # 工作经验
    description = models.TextField(default='', verbose_name='岗位介绍')  # 岗位介绍
    welfare = models.TextField(default='', verbose_name='福利')  # 福利

    company = models.ForeignKey('companies.CompanyInfo', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='公司')
    location = models.ForeignKey('areas.Areas', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='办公地点')

    recommend = models.IntegerField(default=0, verbose_name='推荐指数')  # 推荐指数
    priority = models.BooleanField(default=False, verbose_name='优先推荐')  # 优先推荐

    def __str__(self):
        return f'{self.pid}: {self.post_name}-{self.company}'

    class Meta:
        app_label = 'recruits'
        db_table = 'tb_post_info'
        verbose_name = '岗位信息'
        verbose_name_plural = verbose_name


class PostResume(models.Model):
    """
    投递简历模型
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='resume', verbose_name='用户')
    post = models.ForeignKey(PostInfo, on_delete=models.CASCADE, related_name='resume',
                             null=True, blank=True, verbose_name='岗位')
    status = models.IntegerField(choices=ResumeStatusChoice.choices, default=ResumeStatusChoice.DELIVER,
                                 verbose_name='投递简历状态')

    @staticmethod
    def add(user, post):
        resume = PostResume(user=user, post=post)
        resume.save()
        return resume

    def __str__(self):
        return f'{self.id}: {self.user}-{self.post}'

    class Meta:
        app_label = 'recruits'
        db_table = 'tb_post_resume'
        verbose_name = '投递简历'
        verbose_name_plural = verbose_name
