			$(function() {
				setupEventHandlers();
			});
			
			function setupEventHandlers() {
				$('#addwordbutton').click(sendWord);
			}
			
			function sendWord() {
				var curword = new Object();
				curword.de = $('#defield').val();
				curword.es = $('#esfield').val();
				curword.comment = $('#commentfield').val();
				var jsonToSend = JSON.stringify(curword);
				
				$.ajax({
					url : '../',
					async : true, 
					type : "POST",
					cache : false,
					data : jsonToSend,
					contentType : "application/json; charset=utf-8",
					dataType : "json",
					timeout : 5000,
					context : document.body,
					success : wordWasAdded,
					error : wordAddError
				});	
			}
			
			function wordWasAdded() {
				var oldtext = $('#messages').html();
				var newtext = oldtext + "<p>Word was added";
				$('#messages').html(newtext);			
			}
			
			function wordAddError(jqXHR, status, error) {
				var oldtext = $('#messages').html();
				var newtext = oldtext + "<p>Ajaxfehler: Status " + status + ", Meldung: " + error;
				$('#messages').html(newtext);
			}