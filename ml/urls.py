from django.urls import path

from . import views
from . import chart_views

app_name = 'ml'

urlpatterns = [

    path('data_preparation/', views.render_prep, name='data_preparation'),
    path('notebook-prep/', views.notebook_prep, name='notebook-prep'),

    path('adaboost/', views.render_adaboost, name='adaboost'),
    path('notebook-ada/', views.notebook_adaboost, name='notebook-ada'),

    path('summary/', views.render_summary, name='summary'),
    path('notebook-summary/', views.notebook_summary, name='notebook-summary'),

    path('bayess/', views.render_bayess, name='bayess'),
    path('notebook-bayess/', views.notebook_bayess, name='notebook-bayess'),

    path('kneighbours/', views.render_kn, name='kneighbours'),
    path('notebook-kn/', views.notebook_kn, name='notebook-kn'),

    path('decision-tree/', views.render_tree, name='decision-tree'),
    path('notebook-tree/', views.notebook_tree, name='notebook-tree'),

    path('random-forest/', views.render_rf, name='random-forest'),
    path('notebook-forest/', views.notebook_rf, name='notebook-forest'),

    path('svc/', views.render_svc, name='svc'),
    path('notebook-svc/', views.notebook_svc, name='notebook-svc'),

    path('grid/', views.render_grid, name='grid'),
    path('notebook-grid/', views.notebook_grid, name='notebook-grid'),

    path('ada-reg/', views.render_ada_reg, name='ada-reg'),
    path('notebook-ada-reg/', views.notebook_ada_reg, name='notebook-ada-reg'),

    path('lasso/', views.render_lasso, name='lasso'),
    path('notebook-lasso/', views.notebook_lasso, name='notebook-lasso'),

    path('lr/', views.render_lr, name='lr'),
    path('notebook-lr/', views.notebook_lr, name='notebook-lr'),

    path('summary-reg/', views.render_summary_reg, name='summary-reg'),
    path('notebook-summary-reg/', views.notebook_summary_reg, name='notebook-summary-reg'),

    path('ridge/', views.render_ridge, name='ridge'),
    path('notebook-ridge/', views.notebook_ridge, name='notebook-ridge'),

    path('unsuperv-prep/', views.render_prep_reg, name='prep-reg'),
    path('notebook-prep-reg/', views.notebook_prep_reg, name='notebook-prep-reg'),

    path('eval-ksn/', views.render_eval_ksn, name='eval-ksn'),
    path('notebook-eval-ksn/', views.notebook_eval_ksn, name='notebook-eval-ksn'),

    path('model-ksn/', views.render_model_ksn, name='model-ksn'),
    path('notebook-model-ksn/', views.notebook_model_ksn, name='notebook-model-ksn'),

    path('prep-ksn/', views.render_prep_ksn, name='prep-ksn'),
    path('notebook-prep-ksn/', views.notebook_prep_ksn, name='notebook-prep-ksn'),

    path('db-agglo-km/', views.render_dbagglokm, name='db-agglo-km'),
    path('notebook-db-agglo-km/', views.notebook_dbagglokm, name='notebook-db-agglo-km'),
    path('charts-KMclustDB/', chart_views.serve_chart1, name='charts-KMclustDB'),
    path('charts-KMclustDB2/', chart_views.serve_chart2, name='charts-KMclustDB2'),
    path('charts-KMclustDB3/', chart_views.serve_chart3, name='charts-KMclustDB3'),
    path('charts-KMclustDB4/', chart_views.serve_chart4, name='charts-KMclustDB4'),

    path('pca/', views.render_pca, name='pca'),
    path('notebook-pca/', views.notebook_pca, name='notebook-pca'),
]
