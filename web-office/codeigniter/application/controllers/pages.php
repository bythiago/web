<?php
  class Pages extends CI_Controller {
    function __construct(){
      parent::__construct();
      //load model
      $this->load->model('page_model');
    }

    public function index(){
      $this->get_template('pages/index', FALSE, FALSE);
    }

    public function view($id = NULL){
      $data['data'] = $this->page_model->get_all($id);

      if($data['data']){
        $this->get_template('pages/view', $data);
      } else {
        show_404();
      }
    }

    public function create(){
      //MY_Token
      $this->funcoes->token('submit');

      $this->form_validation->set_rules(
        'nome', 'Nome', 'trim|required|min_length[5]|max_length[50]'
      );

      $this->form_validation->set_rules(
        'quantidade', 'Quantidade', 'trim|numeric|required||max_length[1]'
      );

      $this->form_validation->set_rules(
        'tipo', 'Tipo', 'trim|numeric|required'
      );

      if($this->form_validation->run() === FALSE){
        $this->get_template('pages/create', FALSE, FALSE);
      } else {
        $this->page_model->set_palhas();
        $this->success(array('message' => 'Cadastro realizado com sucesso.', 'type' => 'success'));
      }
    }

    public function update($id = NULL){
      //MY_Token
      $this->funcoes->token('submit');

      $data['data'] = $this->db->get_where('pedido', array('id' => $id))->result();

      if($data['data']){
        $this->form_validation->set_rules(
          'nome', 'Nome', 'trim|required|min_length[5]|max_length[50]'
        );

        $this->form_validation->set_rules(
          'quantidade', 'Quantidade', 'trim|numeric|required||max_length[1]'
        );

        $this->form_validation->set_rules(
          'tipo', 'Tipo', 'trim|numeric|required'
        );

        if($this->form_validation->run() === FALSE){
          $this->get_template('pages/update', $data, TRUE);
        } else {
          $this->page_model->set_update_id();
          $this->success(array('message' => 'Cadastro atualizado com sucesso.', 'type' => 'success'));
        }
      } else {
        show_404();
      }
    }

    public function delete($id){
      if(is_numeric($id)){
        $this->page_model->delete($id);
        $this->success(array('message' => 'Registro deletado com sucesso.', 'type' => 'success'));
      } else {
       show_404();
      }
    }

    public function success($message){
      $this->load->view('templates/header.php');
      $this->load->view('pages/message/success', $message);
      $this->load->view('templates/footer.php');
    }

    public function get_template($page, $data = NULL, $parser = NULL){
      $this->load->view('templates/header.php');
      ($parser) ? $this->parser->parse("$page", $data) : $this->load->view("$page", $data);
      $this->load->view('templates/footer.php');
    }
}
?>