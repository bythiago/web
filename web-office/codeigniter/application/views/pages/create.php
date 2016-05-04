<h2>Formulário</h2>
<div class="form">
  <?php //echo validation_errors(); ?>
  <?php echo form_open('pages/create') ?>
  <div class="form-group">
    <label>Nome</label>
    <?php echo form_error('nome', '<div class="alert alert-danger">' , '</div>'); ?>
    <input type="text" name="nome" class="form-control" value="<?=set_value('nome'); ?>">
  </div>

  <div class="form-group">
    <label>Quantidade</label>
    <?php echo form_error('quantidade', '<div class="alert alert-danger">' , '</div>'); ?>
    <input type="number" name="quantidade" class="form-control" value="<?=set_value('quantidade'); ?>">
  </div>

  <div class="form-group">
    <label>Tipo</label>
    <?php echo form_error('tipo', '<div class="alert alert-danger">' , '</div>'); ?>
    <select name="tipo" class="form-control">
      <option value="" <?php echo set_select('tipo', '', TRUE); ?>>Selecione um item dessa lista</option>
      <option value="1" <?php echo set_select('tipo', '1'); ?> >Cobertura de Chocolate</option>
      <option value="2" <?php echo set_select('tipo', '2'); ?> >Normal</option>
    </select>
  </div>

  <input type="hidden" name="hash" value="<?=$_SESSION['_token'];?>">
  <input type="submit" name="submit" class="btn btn-default" value="Create news item" />
</div>