from flask import Flask, request, render_template_string

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.errorhandler(404)
def page_not_found(e):
    template = """
  <!DOCTYPE html>
<html>

<head>

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>SKF Labs</title>

	<link href="/static/css/Normalize.css" rel="stylesheet">
	<link href="/static/css/datepicker3.css" rel="stylesheet">
	<link href="/static/css/styles.css" rel="stylesheet">

	<!--Icons-->
	<script src="/static/js/lumino.glyphs.js"></script>
	<script src="/static/js/hints.js"></script>
	<link href="https://fonts.googleapis.com/css2?family=Hind:wght@700&display=swap" rel="stylesheet">

</head>

<body>

	<header class="header">
		<div class="wrap wide">
			<div class="inner flx flx-ac flx-jsb">

				<div class="left flx flx-ac">
					<div class="logo">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 75.3 86.9"
							style="enable-background:new 0 0 75.3 86.9" xml:space="preserve">
							<path d="m37.7
									86.9-.7-.4c-.9-.5-1.9-1.1-2.8-1.8-2.7-2-5-4.5-6.6-7.5-1.7-3-2.8-6.2-3.3-9.6
									0-.3-.1-.5-.1-.8-.2.1-.4.2-.7.3-3.1 1.3-6.5 2-9.9 2-3.5
									0-6.8-.7-10-2-1-.4-1.9-.9-2.8-1.4l-.8-.4v-.9c0-1.1.1-2.1.2-3.1.5-3.5
									1.6-6.7 3.3-9.7 1.7-3 3.9-5.6
									6.7-7.6.2-.2.4-.3.6-.5-.2-.2-.4-.3-.7-.5-2.7-2-5-4.6-6.6-7.5-1.8-3-2.9-6.2-3.3-9.6v-.1c-.1-1.1-.2-2.2-.2-3.2v-.9l.7-.4c1-.6
									1.9-1.1 2.9-1.4 3.2-1.3 6.5-2 10-2s6.8.7 9.9 2c.2.1.4.2.7.3 0-.2
									0-.5.1-.7.5-3.4 1.6-6.6 3.3-9.6 1.6-3 3.9-5.6 6.6-7.7 1-.7 1.9-1.2
									2.8-1.8l.7-.4.8.5c.8.5 1.6 1 2.5 1.6 2.8 2.1 5.1 4.7 6.8 7.7 1.7 3 2.8
									6.2 3.2 9.6 0 .3 0 .5.1.8.2-.1.5-.2.7-.3 3.1-1.3 6.5-2 9.9-2 3.5 0
									6.8.7 9.9 2 1 .4 2 .9 2.9 1.5l.7.4v.8c0 1 0 2-.1 3.1v.1c-.5 3.4-1.5
									6.7-3.2 9.6-1.8 3-4 5.5-6.8 7.6-.2.2-.4.3-.6.5.2.2.4.3.6.5 2.7 2 5 4.6
									6.7 7.6 1.7 3 2.8 6.2 3.2 9.7.1 1.1.1 2.1.1 3.1v.9l-.7.4c-.9.5-1.8
									1-2.8 1.4-3.1 1.3-6.4 2-9.9 2s-6.8-.7-10-2c-.2-.1-.5-.2-.7-.3 0 .2 0
									.5-.1.7-.4 3.4-1.5 6.7-3.2 9.7-1.7 3-4 5.6-6.8 7.6-.8.7-1.7 1.3-2.6
									1.8l-.6.3zM27.1 64.3c0 .9 0 1.9.1 2.8.4 2.9 1.4 5.8 3 8.5 1.5 2.6 3.4
									4.9 5.8 6.6.6.4 1.1.8 1.6 1.2.5-.3 1-.7 1.5-1.1 2.5-1.8 4.5-4
									6-6.7s2.5-5.6
									2.9-8.5c.1-.6.1-1.3.1-1.9-1.6-1-3.1-2.2-4.5-3.6-2.4-2.3-4.3-5.1-5.5-8.1-1-2.3-1.6-4.8-1.8-7.3-1.8
									1.3-3.3 2.8-4.7 4.6-1.7 2.3-3 4.9-3.7 7.7-.5 1.9-.8 3.9-.8 5.8zM50.4
									63c.8.4 1.7.9 2.6 1.2 2.8 1.2 5.8 1.8 8.8 1.8 3 0 6-.6 8.7-1.8.6-.3
									1.2-.5 1.7-.8 0-.7
									0-1.3-.1-2-.4-2.9-1.4-5.8-2.9-8.5s-3.5-4.9-5.9-6.7c-.5-.4-1.1-.8-1.6-1.2-1.7.9-3.5
									1.6-5.4 2.1-3.2.9-6.5 1.1-9.8.7-2.5-.3-4.9-1-7.2-2 .2 2.2.8 4.3 1.6 6.3
									1.1 2.7 2.8 5.1 4.9 7.1 1.4 1.6 3 2.8 4.6 3.8zM3 63.4c.6.3 1.2.6 1.8.8
									2.8 1.2 5.7 1.8 8.8 1.8 3 0 6-.6 8.8-1.8.6-.3 1.2-.5 1.8-.8.1-2
									.4-3.9.9-5.8.8-3.2 2.3-6.1 4.2-8.8 1.6-2 3.4-3.8
									5.4-5.3-2-.9-4.1-1.5-6.2-1.7-2.9-.3-5.8-.2-8.7.5-1.8.5-3.6 1.3-5.4
									2.3-.8.5-1.6 1-2.4 1.6-2.4 1.8-4.4 4-5.8 6.7-1.6 2.7-2.6 5.5-3
									8.6-.1.7-.2 1.3-.2 1.9zm37.7-20.1c2 .8 4 1.4 6.2 1.7 2.9.4 5.8.2 8.7-.6
									1.8-.4 3.5-1.1 5.1-2l.4-.2c.7-.4 1.5-1 2.3-1.5 2.4-1.8 4.4-4.1 6-6.7
									1.5-2.6 2.4-5.5 2.8-8.5
									0-.7.1-1.4.1-2-.5-.3-1.1-.6-1.7-.8-2.8-1.2-5.7-1.8-8.8-1.8-3 0-6 .6-8.8
									1.8-.6.2-1.2.5-1.8.8-.1 1.9-.3 3.8-.8 5.7-.9 3.2-2.3 6.2-4.3 8.9-1.6
									2-3.4 3.7-5.4 5.2zM3.1 25.4c.4 3 1.4 5.9 3 8.5 1.5 2.6 3.5 4.9 5.9
									6.7.5.4 1.1.8 1.7 1.1 1.7-.9 3.5-1.6 5.3-2.2 3.3-.8 6.6-1 9.9-.6 2.5.3
									5 1 7.3
									2-.3-2.2-.8-4.3-1.7-6.4-1.1-2.7-2.7-5.1-4.8-7.1-.8-.8-1.6-1.5-2.5-2.2l-2.3-1.5c-.7-.5-1.6-.9-2.4-1.2-2.8-1.2-5.8-1.8-8.8-1.8-3.1
									0-6 .6-8.8 1.8-.6.2-1.2.5-1.8.8-.1.8 0 1.5 0 2.1zm24-3.7c1.7 1 3.2 2.2
									4.6 3.7 2.3 2.3 4.1 5 5.4 8.1 1 2.4 1.6 4.8 1.9 7.3 1.7-1.3 3.3-2.8
									4.6-4.6 1.7-2.4 3-5 3.8-7.8.5-1.9.7-3.9.7-5.8 0-.9
									0-1.9-.1-2.9-.4-2.9-1.3-5.8-2.9-8.4-1.5-2.7-3.5-5-6-6.8-.5-.3-1-.7-1.6-1-.6.3-1.1.7-1.7
									1.1-2.4 1.8-4.3 4.1-5.8 6.7-1.5 2.7-2.5 5.5-3 8.5.2.6.1 1.3.1 1.9z" />
						</svg>
					</div>
					<div class="name pl1">
						Security Knowledge Framework
					</div>
				</div>

				<div class="right flx flx-ac">
					<div class="chat">
						<a href="https://gitter.im/Security-Knowledge-Framework/Lobby" rel="nofollow">
							<img src="/static/img/badge.svg" alt="Join the chat at
										https://gitter.im/Security-Knowledge-Framework/Lobby" data-canonical-src="/static/img/badge.svg">
						</a>
					</div>
					<div class="toggle">
						<input type="checkbox" class="checkbox" id="checkbox">
						<label for="checkbox" class="label">
							<i class="fas fa-moon"></i>
							<i class='fas fa-sun'></i>
							<div class="ball"></div>
						</label>
					</div>
				</div>

			</div>
		</div>
	</header>

	<main class="container">

		<section class="bgg">
			<div class="wrap small">
				<div class="inner pt6 pb6">

               <!-- Start Original Code -->
               <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
                  <div class="row">
                  </div>
                  <!--/.row-->
                  <div class="row">
                     <div class="col-lg-12">
                        <h1 class="page-header">Live demonstration!</h1>
                     </div>
                  </div>
                  <!--/.row-->
                  <div class="row">
                     <div class="col-lg-12">
                        <div class="panel panel-default">
                           <div class="panel-heading">Server side template injection </div>
                           <div class="panel-body">
                              <div class="col-md-6">
								<center>
									<p style="font-size:2em;"> {0} </p>
								</center>
                           </div>
                        </div>
                     </div>
                     <!-- /.col-->
                  </div>
                  <!-- /.row -->
               </div>
               <!--/.main-->
               <!-- End Original Code -->
            </div>
			</div>
		</section>

		<footer class="footer">
			<div class="wrap wide">
				<div class="inner pt3 pb3 text-center">
					&copy; SKF - <a rel="nofollow" href="https://www.securityknowledgeframework.org/"
						target="_blank">Visit
						website</a>
				</div>
			</div>
		</footer>

		<div class="seed">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 75.3 86.9" style="enable-background:new 0 0 75.3 86.9"
				xml:space="preserve">
				<path d="m37.7
									86.9-.7-.4c-.9-.5-1.9-1.1-2.8-1.8-2.7-2-5-4.5-6.6-7.5-1.7-3-2.8-6.2-3.3-9.6
									0-.3-.1-.5-.1-.8-.2.1-.4.2-.7.3-3.1 1.3-6.5 2-9.9 2-3.5
									0-6.8-.7-10-2-1-.4-1.9-.9-2.8-1.4l-.8-.4v-.9c0-1.1.1-2.1.2-3.1.5-3.5
									1.6-6.7 3.3-9.7 1.7-3 3.9-5.6
									6.7-7.6.2-.2.4-.3.6-.5-.2-.2-.4-.3-.7-.5-2.7-2-5-4.6-6.6-7.5-1.8-3-2.9-6.2-3.3-9.6v-.1c-.1-1.1-.2-2.2-.2-3.2v-.9l.7-.4c1-.6
									1.9-1.1 2.9-1.4 3.2-1.3 6.5-2 10-2s6.8.7 9.9 2c.2.1.4.2.7.3 0-.2
									0-.5.1-.7.5-3.4 1.6-6.6 3.3-9.6 1.6-3 3.9-5.6 6.6-7.7 1-.7 1.9-1.2
									2.8-1.8l.7-.4.8.5c.8.5 1.6 1 2.5 1.6 2.8 2.1 5.1 4.7 6.8 7.7 1.7 3 2.8
									6.2 3.2 9.6 0 .3 0 .5.1.8.2-.1.5-.2.7-.3 3.1-1.3 6.5-2 9.9-2 3.5 0
									6.8.7 9.9 2 1 .4 2 .9 2.9 1.5l.7.4v.8c0 1 0 2-.1 3.1v.1c-.5 3.4-1.5
									6.7-3.2 9.6-1.8 3-4 5.5-6.8 7.6-.2.2-.4.3-.6.5.2.2.4.3.6.5 2.7 2 5 4.6
									6.7 7.6 1.7 3 2.8 6.2 3.2 9.7.1 1.1.1 2.1.1 3.1v.9l-.7.4c-.9.5-1.8
									1-2.8 1.4-3.1 1.3-6.4 2-9.9 2s-6.8-.7-10-2c-.2-.1-.5-.2-.7-.3 0 .2 0
									.5-.1.7-.4 3.4-1.5 6.7-3.2 9.7-1.7 3-4 5.6-6.8 7.6-.8.7-1.7 1.3-2.6
									1.8l-.6.3zM27.1 64.3c0 .9 0 1.9.1 2.8.4 2.9 1.4 5.8 3 8.5 1.5 2.6 3.4
									4.9 5.8 6.6.6.4 1.1.8 1.6 1.2.5-.3 1-.7 1.5-1.1 2.5-1.8 4.5-4
									6-6.7s2.5-5.6
									2.9-8.5c.1-.6.1-1.3.1-1.9-1.6-1-3.1-2.2-4.5-3.6-2.4-2.3-4.3-5.1-5.5-8.1-1-2.3-1.6-4.8-1.8-7.3-1.8
									1.3-3.3 2.8-4.7 4.6-1.7 2.3-3 4.9-3.7 7.7-.5 1.9-.8 3.9-.8 5.8zM50.4
									63c.8.4 1.7.9 2.6 1.2 2.8 1.2 5.8 1.8 8.8 1.8 3 0 6-.6 8.7-1.8.6-.3
									1.2-.5 1.7-.8 0-.7
									0-1.3-.1-2-.4-2.9-1.4-5.8-2.9-8.5s-3.5-4.9-5.9-6.7c-.5-.4-1.1-.8-1.6-1.2-1.7.9-3.5
									1.6-5.4 2.1-3.2.9-6.5 1.1-9.8.7-2.5-.3-4.9-1-7.2-2 .2 2.2.8 4.3 1.6 6.3
									1.1 2.7 2.8 5.1 4.9 7.1 1.4 1.6 3 2.8 4.6 3.8zM3 63.4c.6.3 1.2.6 1.8.8
									2.8 1.2 5.7 1.8 8.8 1.8 3 0 6-.6 8.8-1.8.6-.3 1.2-.5 1.8-.8.1-2
									.4-3.9.9-5.8.8-3.2 2.3-6.1 4.2-8.8 1.6-2 3.4-3.8
									5.4-5.3-2-.9-4.1-1.5-6.2-1.7-2.9-.3-5.8-.2-8.7.5-1.8.5-3.6 1.3-5.4
									2.3-.8.5-1.6 1-2.4 1.6-2.4 1.8-4.4 4-5.8 6.7-1.6 2.7-2.6 5.5-3
									8.6-.1.7-.2 1.3-.2 1.9zm37.7-20.1c2 .8 4 1.4 6.2 1.7 2.9.4 5.8.2 8.7-.6
									1.8-.4 3.5-1.1 5.1-2l.4-.2c.7-.4 1.5-1 2.3-1.5 2.4-1.8 4.4-4.1 6-6.7
									1.5-2.6 2.4-5.5 2.8-8.5
									0-.7.1-1.4.1-2-.5-.3-1.1-.6-1.7-.8-2.8-1.2-5.7-1.8-8.8-1.8-3 0-6 .6-8.8
									1.8-.6.2-1.2.5-1.8.8-.1 1.9-.3 3.8-.8 5.7-.9 3.2-2.3 6.2-4.3 8.9-1.6
									2-3.4 3.7-5.4 5.2zM3.1 25.4c.4 3 1.4 5.9 3 8.5 1.5 2.6 3.5 4.9 5.9
									6.7.5.4 1.1.8 1.7 1.1 1.7-.9 3.5-1.6 5.3-2.2 3.3-.8 6.6-1 9.9-.6 2.5.3
									5 1 7.3
									2-.3-2.2-.8-4.3-1.7-6.4-1.1-2.7-2.7-5.1-4.8-7.1-.8-.8-1.6-1.5-2.5-2.2l-2.3-1.5c-.7-.5-1.6-.9-2.4-1.2-2.8-1.2-5.8-1.8-8.8-1.8-3.1
									0-6 .6-8.8 1.8-.6.2-1.2.5-1.8.8-.1.8 0 1.5 0 2.1zm24-3.7c1.7 1 3.2 2.2
									4.6 3.7 2.3 2.3 4.1 5 5.4 8.1 1 2.4 1.6 4.8 1.9 7.3 1.7-1.3 3.3-2.8
									4.6-4.6 1.7-2.4 3-5 3.8-7.8.5-1.9.7-3.9.7-5.8 0-.9
									0-1.9-.1-2.9-.4-2.9-1.3-5.8-2.9-8.4-1.5-2.7-3.5-5-6-6.8-.5-.3-1-.7-1.6-1-.6.3-1.1.7-1.7
									1.1-2.4 1.8-4.3 4.1-5.8 6.7-1.5 2.7-2.5 5.5-3 8.5.2.6.1 1.3.1 1.9z" />
			</svg>
		</div>

	</main>

	<script src="/static/js/jquery-3.6.0.min.js"></script>
	<script src="/static/js/bootstrap.min.js"></script>
</body>

</html>

""".format(request.url)
    return render_template_string(template), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0')
