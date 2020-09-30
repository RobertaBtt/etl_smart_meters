%include header.tpl
%import time

				<div class="row">
					<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">


						<div class="panel panel-default">
							<!-- Default panel contents -->
							<div class="panel-heading"><span class="glyphicon glyphicon-list" aria-hidden="true"></span><b>&nbsp;Message list for MSG_CLASS-ID {{msg_id}} ({{msg_name}})</b></div>
							<div class="panel-body">
								<small>Data fetched on: &nbsp;
								<span class="glyphicon glyphicon-time" aria-hidden="true"></span>
								{{time.ctime(time.time())}}
</small>
							</div>

							<!-- Table -->
							<table class="table">


									<thead>
										<tr>
											<th>HASH</th>
											<th>Sender</th>
											<th>Measured</th>
											<th>Sent</th>
											<th>Received</th>
											<th>Processed</th>
										</tr>
									</thead>

								%for m in msg:
								<tr>
									<td>
										<a href="/message/{{msg_id}}/{{m['payload_hash']}}">
										{{m.get('payload_hash', '')}}
										</a>
									</td>
									<td>{{m.get('sender_id', '')}}</td>
									<td>{{time.ctime(m.get('measurement_ts'))}}</td>
									<td>{{time.ctime(m.get('send_ts'))}}</td>
									<td>{{time.ctime(m.get('receive_ts'))}}</td>
									<td>{{time.ctime(m.get('elaborated_ts'))}}</td>
								</tr>
								%end

							</table>
						</div>


					</div>

				</div>
				<div>
				</div>
				<!-- jQuery -->
				<script src="//code.jquery.com/jquery.js"></script>
				<!-- Bootstrap JavaScript -->
				<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
			</body>
			</html>