<?php
  class Page_model extends CI_Model {

    function __construct(){
      parent::__construct();
      $this->load->database();
    }

    public function get_all($id){
      if ($id){
        //ONLY ID
        $query = $this->db->get_where('pedido', array('id' => $id));
      } else {
        //ALL
        $this->db->order_by('id' , 'desc');
        $query = $this->db->get('pedido', 10);
      }
      return $query->result();
    }

    public function set_palhas(){
      $data2 = array(
        'nome'       => $this->input->post('nome'),
        'quantidade' => $this->input->post('quantidade'),
        'tipo'       => $this->input->post('tipo'),
      );

      return $this->db->insert('pedido', $data2);
    }

    public function set_update_id(){
      $data2 = array(
        'id'         => $this->input->post('id'),
        'nome'       => $this->input->post('nome'),
        'quantidade' => $this->input->post('quantidade'),
        'tipo'       => $this->input->post('tipo'),
      );

      return $this->db->update('pedido', $data2, array('id' => $data2['id']));
    }

    public function delete($id){
      return $this->db->delete('pedido', array('id' => $id));
    }
}
?>
