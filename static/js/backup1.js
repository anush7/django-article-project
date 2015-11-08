$(function () {
	var preview_width = 200;
	var min_cropper_width = 300;
	var aspectRatio = 1;
    $('#fileupload').fileupload({
        dataType: 'json',
        formData: [{
		        name: 'csrfmiddlewaretoken',
		        value: '{{csrf_token}}'
		}],
        add: function (e, data) {
            //data.context = $('<p/>').text('Uploading...').appendTo('#progress');

            var template = "";
            template += '<div class="cropper_ajax_ctrl img_holder"></div>'
           	template += '<div class="preview_holder"><div class="cropper-preview cropper_controls"></div></div>'
           	data.list = $('<li style="width: 70%;" />').html(template);
           	$('#coverUploader').append(data.list);
            data.submit();
        },
        done: function (e, data) {
        	//data.context.text('Upload finished.');
        	//data.context.fadeOut();
            //$("<p><img src='"+data.result.file+"' width='260px'/></p>").appendTo('#id_photos');
            console.log(data)
            data.list.find('.img_holder').append('<img src="'+data.result.file+'" id="cover_img" class="cropper fade"/>');
            setTimeout(function(){
            	data.list.find('img').addClass('in');
            	$("#coverUploader .cropper_controls.cropper-preview")
            		.css("width", preview_width)
		    		.css("height", preview_width / aspectRatio)
		    		.css("overflow", "hidden");
            	$("#coverUploader .preview_holder")
            		.css("width", preview_width)
            		.css("height", preview_width / aspectRatio);
            	$("#coverUploader .cropper").cropper({
				    aspectRatio: aspectRatio,
				    minWidth: min_cropper_width,
				    minHeight: min_cropper_width / aspectRatio,
				    preview: ".cropper-preview",
				    done: function(data) {
				    	$('#logo_x1').val(data.x);
				    	$('#logo_y1').val(data.y);
				    	$('#logo_x2').val(data.x + data.width);
				    	$('#logo_y2').val(data.y + data.height);
				    }
				});
            	setTimeout(function(){
		    		$("#coverUploader .cropper_controls.cropper-preview img").css("max-width", 'none');
            	}, 2000);
            },300);

        },
        progressall: function (e, data) {
	        //var progress = parseInt(data.loaded / data.total * 100, 10);
	        //$('#progress .bar').css('height','18px');
	        //$('#progress .bar').css('width',progress + '%');
	        //$('#progress').fadeOut();
    	}
    });
});