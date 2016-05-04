<?php
  class Pages extends CI_Controller {
    function __construct(){
      parent::__construct();
      //load model
      $this->load->model('page_model');
    }

    public function view($id = NULL){
      $data['data'] = $this->page_model->get_all($id);

      if($data['data']){
        $this->get_template('pages/index', $data);
        // $this->load->view('templates/header.php');
        // $this->parser->parse('pages/index', $data);
        // $this->load->view('templates/footer.php');
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
        $this->load->view('templates/header.php');
        $this->load->view('pages/create');
        $this->load->view('templates/footer.php');
      } else {
        $this->page_model->set_palhas();
        $this->success(array('message' => 'Cadastro realizado com sucesso.', 'type' => 'success'));
        // redirect('pages/success', 'location', 301);
        //$this->load->view('pages/create/success');
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
          $this->load->view('templates/header.php');
          $this->parser->parse('pages/update', $data);
          $this->load->view('templates/footer.php');
        } else {
          $this->page_model->set_update_id();
          $this->success(array('message' => 'Cadastro atualizado com sucesso.', 'type' => 'success'));
        }
      } else {
        show_404();
      }
    }

    public function success($message){
      $this->load->view('templates/header.php');
      $this->load->view('pages/create/success', $message);
      $this->load->view('templates/footer.php');
    }

    public function get_template($page, $data = NULL){
      $this->load->view('templates/header.php');
      $this->parser->parse("$page", $data);
      $this->load->view('templates/footer.php');
    }
}
?>