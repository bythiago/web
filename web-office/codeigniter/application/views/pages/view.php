<div class="starter-template">
<h1>Bootstrap starter template</h1>
<p class="lead">Use this document as a way to quickly start any new project.<br> All you get is this text and a mostly barebones HTML document.</p>
</div>
<table class="table table-bordered table-hover">
  <thead>
    <tr class="active">
      <th>id</th>
      <th>nome</th>
      <th>quantidade</th>
      <th>tipo</th>
      <th>editar</th>
      <th>deletar</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($data as $d):?>
      <tr>
        <td><?=$d->id;?></td>
        <td><?=$d->nome;?></td>
        <td><?=$d->quantidade;?></td>
        <td><?=$this->funcoes->get_tipo($d->tipo);?></td>
        <td width="1"><a href="<?=base_url("pages/update/{$d->id}");?>" class="btn btn-success">editar</a></td>
        <td width="1"><a href="<?=base_url("pages/delete/{$d->id}");?>" class="btn btn-danger" onclick="return confirm('Tem certeza de que deseja deletar esse registro?')">deletar</a></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>