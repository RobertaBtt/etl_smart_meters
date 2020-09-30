%import time
%from decimal import Decimal
%include header.tpl


<h1 xmlns="http://www.w3.org/1999/html" class="text-center text-info">Message <b>{{msg.get('payload_hash','')}}</b></h1>
    <br/>
    <div class="row">
        <div class="col-md-6">
            <ul class="list-group">
                <li class="list-group-item list-group-item-info"><span class="glyphicon glyphicon-time"></span>&nbsp;Times</li>
                <li class="list-group-item"><b>Measured</b>:&nbsp; <span class="badge company">{{time.ctime(msg.pop('measurement_ts'))}}</span></li>
                <li class="list-group-item"><b>Sent</b>:&nbsp; <span class="badge company">{{time.ctime(msg.pop('send_ts',0))}}</span></li>
                <li class="list-group-item"><b>Received</b>:&nbsp; <span class="badge company">{{time.ctime(msg.pop('receive_ts'))}}</span></li>
                <li class="list-group-item"><b>Processed</b>:&nbsp; <span class="badge company">{{time.ctime(msg.pop('elaboration_ts'))}}</span></li>

            </ul>

            <ul class="list-group">
                <li class="list-group-item list-group-item-info"><span class="glyphicon glyphicon-info-sign"></span>&nbsp;Other metadata</li>
                <li class="list-group-item"><b>Topic</b>:&nbsp; <span class="badge company">{{msg.pop('topic')}}</span></li>
                <li class="list-group-item"><b>Sender ID</b>:&nbsp; <span class="badge company">{{msg.pop('sender_id')}}</span></li>
                <li class="list-group-item"><b>Message Class ID</b>:&nbsp; <span class="badge company">{{msg.pop('msg_id')}} ({{msg_name}})</span></li>
                <li class="list-group-item"><b>CRC</b>:&nbsp; <span class="badge company">{{msg.pop('CRC')}}</span></li>
                <li class="list-group-item"><b>Content Length</b>:&nbsp; <span class="badge company">{{msg.pop('content_length')}}</span></li>
                <li class="list-group-item"><b>API version</b>:&nbsp; <span class="badge company">{{msg.pop('API_version')}}</span></li>
                <li class="list-group-item"><b>Hash (MD5)</b>:&nbsp; <span class="badge company">{{msg.pop('payload_hash')}}</span></li>
            </ul>

        </div>
        <div class="col-md-6">
            %if msg_id != '30':
            <ul class="list-group">
                 <li class="list-group-item list-group-item-info"><span class="glyphicon glyphicon-list"></span>&nbsp;Data</li>
            %for k,v in msg.items():
                %if k.endswith('ts'):
                <li class="list-group-item"><b>{{k}}</b>:&nbsp; <span class="badge company">{{time.ctime(v)}}</span></li>
                %elif type(v) in (Decimal, float):
                <li class="list-group-item"><b>{{k}}</b>:&nbsp; <span class="badge company">{{'%.2f' % v}}</span></li>
                %else:
                <li class="list-group-item"><b>{{k}}</b>:&nbsp; <span class="badge company">{{v}}</span></li>
                %end
            %end
            %else:
            <ul class="list-group">
                 <li class="list-group-item list-group-item-info"><span class="glyphicon glyphicon-list"></span>&nbsp;Data</li>
            %for k,v in msg.items():
                %if v:
                <li class="list-group-item"><b>{{k}}</b>:&nbsp; <span class="badge e_warning"><span class="glyphicon glyphicon-warning-sign"></span></span></li>
                %else:
                <li class="list-group-item"><b>{{k}}</b>:&nbsp; <span class="badge e_success"><span class="glyphicon glyphicon-ok"></span></span></li>
                %end
            %end
            %end
            </ul>
        </div>
    </div>

</body>
</html>