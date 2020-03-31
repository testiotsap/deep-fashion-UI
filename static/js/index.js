$(document).ready(() => {
	// Variables
	// video = document.getElementById("video");
	// canvas = document.getElementById("canvas");
	// context = canvas.getContext("2d");
	// video = document.getElementById("video");
	clickImageBtn = document.getElementById("clickImageBtn");
	inputImage = document.getElementById("inputImage");

	$("#selectImageBtn").click(event => {
		event.preventDefault();
		$("#select").trigger("click");
	});

	$("#select").change(event => {
		$("#inputImage").removeClass("d-none");
		inputImage.src = URL.createObjectURL(event.target.files[0]);
		$("#searchBtn").prop("disabled", false);
		$("#selectImageBtn").html("Change Image");
		$(".btn").css("top", "100%");
	});

	// $("#openCameraBtn").click(event => {
	//   event.preventDefault();
	//   overlayOn();
	// });

	// $("#canvasSubmitBtn").click(event => {
	//   event.preventDefault();
	//   overlayOff();
	//   // $("#searchBtn").trigger("click");
	//   const image = new Image();
	//   dataUrl = canvas.toDataURL("image/png");
	//   image.src = dataUrl;
	//   inputImage.src = image.src;
	//   $("#inputImage").removeClass("d-none");
	//   // console.log(dataUrl);

	//   // canvas.toBlob(blob => {
	//   //   image = document.createElement("img");
	//   //   url = URL.createObjectURL(blob);

	//   //   image.onload = function() {
	//   //     URL.revokeObjectURL(url);
	//   //   };

	//   //   image.src = url;
	//   //   $("#inputImage").removeClass("d-none");
	//   //   inputImage.src = image.src;
	//   // });
	//   $("#searchBtn").prop("disabled", false);
	// });

	// $("#cancel").click(event => {
	//   event.preventDefault();
	//   overlayOff();
	// });
	// $("#searchBtn").click(() => {
	//   sendData(dataUrl);
	// });
});

// function sendData(dataUrl) {
//   console.log(dataUrl);
//   imgData = {
//     img: dataUrl
//   };
//   $.ajax({
//     url: "/",
//     method: "POST",
//     dataType: "json",
//     data: JSON.stringify(imgData),
//     success: response => {
//       console.log(response);
//       // $("html").html(response);
//     },
//     error: error => {
//       console.log(error);
//     }
//   });
// }

// function openCamera() {
//   // var video = document.getElementById("video");

//   if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
//       video.srcObject = stream;
//       video.play();
//     });
//   }

//   clickImageBtn.addEventListener("click", function(event) {
//     event.preventDefault();
//     $("#canvasDiv").removeClass("d-none");
//     context.drawImage(video, 0, 0, 400, 300);
//     clickImageBtn.innerHTML = "Try Again";
//     $("#canvasSubmitBtn").removeClass("d-none");
//   });
// }

// function closeCamera() {
//   video.pause();
//   video.src = "";
// }

// function overlayOn() {
//   document.getElementById("overlay").style.display = "block";
//   openCamera();
// }

// function overlayOff() {
//   document.getElementById("overlay").style.display = "none";
//   closeCamera();
// }
