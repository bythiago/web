<?php $base = $_SERVER['REQUEST_URI']; ?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PEC | Geografia Legal</title>

  <!-- Bootstrap CSS -->
  <link href="<?=$base?>/assets/components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="<?=$base?>/assets/components/Bootflat/bootflat/css/bootflat.min.css" rel="stylesheet">
  <link href="<?=$base?>/dist/css/docs.css" rel="stylesheet">

  <!-- jQuery -->
  <script src="<?=$base?>/assets/components/jquery/dist/jquery.js"></script>
  <link rel="stylesheet" href="http://blackrockdigital.github.io/startbootstrap-creative/font-awesome/css/font-awesome.min.css" type="text/css">
  <link href="<?=$base?>/dist/css/main.min.css" rel="stylesheet">
  <link href="<?=$base?>/dist/css/carousel.css" rel="stylesheet">
  <link href="<?=$base?>/assets/components/animate.css/animate.min.css" rel="stylesheet">
  <link href="<?=$base?>/dist/css/scrolling-nav.css" rel="stylesheet">
  <link href="http://getbootstrap.com.br/assets/css/src/docs.css" rel="stylesheet">
  <!-- Google Fonts | Lato -->
  <link href='https://fonts.googleapis.com/css?family=Lato|Alegreya+Sans' rel='stylesheet' type='text/css'>
</head>
<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">
<!-- Navigation -->
<nav class="navbar navbar-default navbar-fixed-top navbar-custom" role="navigation">
  <div class="container">
    <div class="navbar-header page-scroll">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
        <span class="sr-only">
          Toggle navigation
        </span>
        <span class="icon-bar">
        </span>
        <span class="icon-bar">
        </span>
        <span class="icon-bar">
        </span>
      </button>
      <!-- <a class="navbar-brand page-scroll" href="#page-top">Start Bootstrap</a> -->
      <div class="nav-logo">
        <a class="page-scroll" href="<?=$base?>"><img src="<?=$base?>/images/logo.png" alt="logo"></a>
      </div>
    </div>
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse navbar-ex1-collapse">
      <ul class="nav navbar-nav">
        <!-- Hidden li included to remove active class from about link when scrolled
        up past about section -->
        <li><a class="page-scroll" href="#page-top">Página Inicial</a></li>
        <li><a class="page-scroll" href="#objetivo">Objetivo</a></li>
        <!-- <li><a class="page-scroll" href="#services">Jogos</a></li> -->
      </ul>
    </div>
    <!-- /.navbar-collapse -->
  </div>
  <!-- /.container -->
</nav>

<div class="container-fluid">
  <div class="row content">
    <?php if (file_exists('conteudo.php'))
      require_once('conteudo.php');
    ?>
  </div>
</div>

<footer id="footer">
<div class="footer-copyright">
  <div class="container">
    <div class="row">
      <div class="col-md-7">
        <p>
          <ul>
          <li>Projeto de Extensão à Comunidade <?=date('Y')?>.</li>
          <li>Professor Jason.</li>
          <br>
          <li><h4>Alunos</h4></li>
          <li>Arthur Silva</li>
          <li>Glauber Henrique</li>
          <li>Juliano Gonçalves</li>
          <li>Thiago Vieira</li>
          <li>Thier Garcia</li>
          </ul>
        </p>
      </div>
      <div class="col-md-5">
        <!-- <nav id="footer-menu">
          <ul>
            <li>
              <a href="#">FAQ's</a>
            </li>
            <li>
              <a href="#">Sitemap</a>
            </li>
            <li>
              <a href="#">Contact</a>
            </li>
          </ul>
        </nav> -->
      </div>
    </div>
  </div>
</div>
</footer>
<script>
jQuery(document).ready(function($) {
  $('.carousel').carousel({
    interval: 4000
  })
});
</script>

<!-- Bootstrap JavaScript -->
<script src="<?=$base?>/assets/components/bootstrap/dist/js/bootstrap.min.js"></script>
<!-- wow.min.js -->
<script src="http://blackrockdigital.github.io/startbootstrap-creative/js/jquery.fittext.js"></script>
<script src="http://blackrockdigital.github.io/startbootstrap-creative/js/wow.min.js"></script>
<script src="http://blackrockdigital.github.io/startbootstrap-creative/js/creative.js"></script>
<!-- scrolling-nav -->
<script src="http://blackrockdigital.github.io/startbootstrap-scrolling-nav/js/jquery.easing.min.js"></script>
<script src="http://blackrockdigital.github.io/startbootstrap-scrolling-nav/js/scrolling-nav.js"></script>
</body>
</html>