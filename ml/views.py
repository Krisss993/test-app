from django.shortcuts import render
import os
from django.http import HttpResponse

def render_prep(request):
    return render(request, 'ml/superv_class/data_preparation.html')

def notebook_prep(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/data_preparation.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_adaboost(request):
    return render(request, 'ml/superv_class/adaboost.html')

def notebook_adaboost(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/adaboost.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_kn(request):
    return render(request, 'ml/superv_class/kn.html')

def notebook_kn(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/KN.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_svc(request):
    return render(request, 'ml/superv_class/svc.html')

def notebook_svc(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/SVC.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_tree(request):
    return render(request, 'ml/superv_class/tree.html')

def notebook_tree(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/tree.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_rf(request):
    return render(request, 'ml/superv_class/rf.html')

def notebook_rf(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/RF.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_bayess(request):
    return render(request, 'ml/superv_class/bayes.html')

def notebook_bayess(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/bayess.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_summary(request):
    return render(request, 'ml/superv_class/summary.html')

def notebook_summary(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/summary.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_ada_reg(request):
    return render(request, 'ml/superv_reg/ada_reg.html')

def notebook_ada_reg(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/ada-reg.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_ridge(request):
    return render(request, 'ml/superv_reg/ridge.html')

def notebook_ridge(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/ridge.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_lr(request):
    return render(request, 'ml/superv_reg/lr.html')

def notebook_lr(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/lr.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_lasso(request):
    return render(request, 'ml/superv_reg/lasso.html')

def notebook_lasso(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/lasso.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_grid(request):
    return render(request, 'ml/superv_reg/grid.html')

def notebook_grid(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/grid_search.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_summary_reg(request):
    return render(request, 'ml/superv_reg/summary_reg.html')

def notebook_summary_reg(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/summary_reg.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_prep_reg(request):
    return render(request, 'ml/superv_reg/prep.html')

def notebook_prep_reg(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/unsuperv_prep.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_prep_ksn(request):
    return render(request, 'ml/ksn/prep.html')

def notebook_prep_ksn(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/KSN_prep.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_model_ksn(request):
    return render(request, 'ml/ksn/model.html')

def notebook_model_ksn(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/KSN_model.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_eval_ksn(request):
    return render(request, 'ml/ksn/eval.html')

def notebook_eval_ksn(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/KSN_eval.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_dbagglokm(request):
    return render(request, 'ml/unsuperv/dbagglokm.html')

def notebook_dbagglokm(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/DBclustKM.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_pca(request):
    return render(request, 'ml/unsuperv/pca.html')

def notebook_pca(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/PCA.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_tsne(request):
    return render(request, 'ml/unsuperv/tsne.html')

def notebook_tsne(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/tsne.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_apriori(request):
    return render(request, 'ml/unsuperv/apriori.html')

def notebook_apriori(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/apriori.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_isoforest(request):
    return render(request, 'ml/unsuperv/forest.html')

def notebook_isoforest(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/isoforest.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_lof(request):
    return render(request, 'ml/unsuperv/lof.html')

def notebook_lof(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/lof.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)


def render_gan_param(request):
    return render(request, 'ml/gan/gan-param.html')

def notebook_gan_param(request):
    # Serve the notebook HTML file
    notebook_file_path = os.path.join('static', 'notebooks/GAN.html')
    with open(notebook_file_path, 'r', encoding='utf-8') as f:
        notebook_html = f.read()
    return HttpResponse(notebook_html)