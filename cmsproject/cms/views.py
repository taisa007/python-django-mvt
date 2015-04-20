# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.models import Entry
from cms.forms import EntryForm

def entry_list(request):
    entries = Entry.objects.all().order_by('id')
    return render_to_response('cms/entry_list.html',   # 使用するテンプレート
        {'entries': entries},    # テンプレートに渡すデータ
        context_instance=RequestContext(request))  # その他標準のコンテキスト

def entry_edit(request, entry_id=None):
    if entry_id:   # entry_id が指定されている (修正時)
        entry = get_object_or_404(Entry, pk=entry_id)
    else:         # team_id が指定されていない (追加時)
        entry = Entry()

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            entry = form.save(commit=False)
            entry.save()
            return redirect('cms:entry_list')
    else:    # GET の時
        form = EntryForm(instance=entry)  # entry インスタンスからフォームを作成

    return render_to_response('cms/entry_edit.html',
                              dict(form=form, entry_id=entry_id),
                              context_instance=RequestContext(request))

def entry_del(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.delete()
    return redirect('cms:entry_list')