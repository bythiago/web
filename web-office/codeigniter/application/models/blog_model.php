<?php
class Blog_model extends CI_Model {

  // public function __construct(){
  //   $this->load->database();
  // }

  public function get_news($numero, $ano) {
    $query = "SELECT id, numero_processo, ano_processo, nome_adquirente, nome_proprietario, logradouro, numero,
    complemento, condominio, bairro, municipio, uf FROM lda_laudo_avaliacao WHERE numero_processo = ? and ano_processo = ?";

    $query = $this->db->query($query, array($numero, $ano));
    return $query->result_array();
  }

}