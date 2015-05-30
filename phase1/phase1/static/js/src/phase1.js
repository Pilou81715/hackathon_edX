/* Javascript for Phase1XBlock. */
function Phase1XBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

   

    $('#submit1', element).click(function(eventObject) {
        var n1 = parseInt( $('#note1').val() | 0);
        var n2 = parseInt( $('#note2').val() | 0);
        var n3 = parseInt( $('#note3').val() | 0);
        if (n1 + n2 + n3 != 10) 
        	alert("Vous n'avez pas réparti les 10 points entre les trois questions");
        else {
        	$('#phase1').hide();
        	$('#phase2').show();
        	var urlH = runtime.handlerUrl(element, 'validate1');
        	var dataP = JSON.stringify({"rep1": "coucou"});
        	$.ajax({
        		type: "POST",
        		url: urlH,
        		data: dataP
        		/*
        		
        		data: JSON.stringify({"rep1": $('#rep1').val(),
        							  "rep2": $('#rep2').val(),
        							  "rep3": $('#rep3').val()} )
        		*/
        	});
        
        }
    });
    
    $('#submit2', element).click(function(eventObject) {
    	$('#phase2').hide();
        $('#phase3').show();
	});
	$('#submit3', element).click(function(eventObject) {
    	$('#phase3').hide();
        $('#finish').show();
	});
    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
