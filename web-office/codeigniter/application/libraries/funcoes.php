<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class MY_Funcoes {
  public function set_selected($value, $selected ){
    return ($value == $selected) ? ' selected="selected"' : '';
  }

  public function get_tipo($key = NULL, $array = array(
      1  => 'Cobertura de Chocolate' ,
      2  => 'Normal' ,
    )){

    if (!$key)
      return $array;
    else
      return $array[$key];
  }

  public function get_value_post_db($value, $post){
    return (empty($post) ? $value : $post);
  }

  public function token($name){
    session_start();
    try {
      $_SESSION['_token'] = (!isset($_SESSION['_token'])) ? hash('sha512', rand(0, 10000)) : $_SESSION['_token'];

      if(isset($_REQUEST[$name])){
        if (strcmp($_SESSION['_token'], $_REQUEST['hash']) != 0 ){
          show_404();
        } else {
          $_SESSION['_token'] = hash('sha512', rand(0, 10000));
        }
      }
    } catch (Exception $e) {
      echo 'Exceção capturada: ',  $e->getMessage(), "\n";
    }
  }
}
/* End of file Funcoes.php */