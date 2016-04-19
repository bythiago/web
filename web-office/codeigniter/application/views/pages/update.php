{data}
<h2>Formulário</h2>
<div class="form">
  <?php echo form_open("pages/update/{$data[0]->id}") ?>
  <div class="form-group">
    <label>Nome</label>
    <?php echo form_error('nome', '<div class="alert alert-danger">' , '</div>'); ?>
    <input type="text" name="nome" class="form-control" value='<?=$this->funcoes->get_value_post_db("{nome}", $this->input->post("nome"));?>'>
  </div>

  <div class="form-group">
    <label>Quantidade</label>
    <?php echo form_error('quantidade', '<div class="alert alert-danger">' , '</div>'); ?>
    <input type="number" name="quantidade" class="form-control" value='<?=$this->funcoes->get_value_post_db("{quantidade}", $this->input->post("quantidade"));?>'>
  </div>

  <div class="form-group">
    <label>Tipo</label>
    <?php echo form_error('tipo', '<div class="alert alert-danger">' , '</div>'); ?>
    <select name="tipo" class="form-control">
      <option value=""  <?=set_select('tipo','1', ($data[0]->tipo == ''));?>>Selecione um item dessa lista</option>
      <option value="1" <?=set_select('tipo','1', ($data[0]->tipo == '1'));?>>Cobertura de Chocolate</option>
      <option value="2" <?=set_select('tipo','2', ($data[0]->tipo == '2'));?> >Normal</option>
    </select>
  </div>

  <input type="hidden" name="id" value="<?=$data[0]->id;?>" />
  <input type="hidden" name="hash" value="<?=$_SESSION['_token'];?>">
  <input type="submit" name="submit" class="btn btn-primary" value="Create news item" />
</div>
{/data}