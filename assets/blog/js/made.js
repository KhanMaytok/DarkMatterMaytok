// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Plugins

(function ($) {
    'use strict';
    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Navigation

    // Global vars
    let body = $('body');
    let navTarget = body.attr('data-page-url');
    let docTitle = document.title;
    let History = window.History;


    // State change event
    History.Adapter.bind(window, 'statechange', function (e) {
        let state = History.getState();
        // console.log(state);

        // Loading state
        body.addClass('loading');

        // Load the page
        $('.page-loader').load(state.hash + ' .page__content', function () {

            // Scroll to top
            $('body, html').animate({
                scrollTop: 0
            }, 300);

            // Find transition time
            let transitionTime = 400;

            // After current content fades out
            setTimeout(function () {

                // Remove old content
                $('.page .page__content').remove();

                // Append new content
                $('.page-loader .page__content').appendTo('.page');

                // Set page URL
                body.attr('data-page-url', window.location.pathname);

                // Update navTarget
                navTarget = body.attr('data-page-url');

                // Set page title
                docTitle = $('.page__content').attr('data-page-title');
                document.title = docTitle;

                // Run page functions
                pageFunctions();

            }, transitionTime);

        });

    });


    // On clicking a link

    if (body.hasClass('ajax-loading')) {
        $(document).on('click', 'a', function (event) {
            // Don't follow link
            event.preventDefault();

            // Get the link target
            let thisTarget = $(this).attr('href');

            // If we don't want to use ajax, or the link is an anchor/mailto/tel
            if ($(this).hasClass('js-no-ajax') || /^#/.test(thisTarget) || thisTarget.indexOf("mailto:") >= 0 || thisTarget.indexOf("tel:") >= 0) {

                // Use the given link
                window.location = thisTarget;
            }

            // if it's a contact modal
            else if ($(this).hasClass('js-contact')) {

                // Open contact modal
            }

            // If link is handled by some JS action – e.g. fluidbox
            else if ($(this).is('.gallery__item__link')) {

                // Let JS handle it
            }

            // If link is external
            else if (thisTarget.indexOf('http') >= 0) {

                // Go to the external link
                window.open(thisTarget, '_blank');

            }

            // If link is internal
            else {

                // Change navTarget
                navTarget = thisTarget;

                // Switch the URL via History
                History.pushState(null, docTitle, thisTarget);
            }

        });

    }


    // Modals
    function lockPage() {
        $('.page').addClass('locked');
        body.addClass('locked');
    }

    function unlockPage() {
        $('.page').removeClass('locked');
        body.removeClass('locked');
    }

    $(document).on('click', '.js-contact', function (event) {
        event.preventDefault();

        body.removeClass('menu--open');
        $('.contact').addClass('visible');
        lockPage();

        $('.button--close-modal').on('click', function () {
            $('.contact').removeClass('visible');
            unlockPage();
        });
    });


    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Page load
    function pageFunctions() {
        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Set UTC to local time
        $('time').each(function () {
            let utc = $(this).attr('data-utc');
            let gmtDateTime = moment.utc(utc, "YYYY-MM-DD HH");
            let local = gmtDateTime.local().format('MMM DD, YYYY');
            $(this).text(local);
        });
        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Show content

        // Wait until first image has loaded
        $('.page__content').find('.hero__image').imagesLoaded({background: true}, function () {

            // Portfolio grid layout
            $('.portfolio-wrap').imagesLoaded(function () {
                $('.portfolio-wrap').masonry({
                    itemSelector: '.portfolio-item',
                    transitionDuration: 0
                });
            });

            // Blog grid layout
            $('.blog-wrap').imagesLoaded(function () {
                $('.blog-wrap').masonry({
                    itemSelector: '.blog-post',
                    transitionDuration: 0
                });
            });

            // Show the content
            body.removeClass('loading');

            // Hide the menu
            body.removeClass('menu--open');
        });


        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Active links

        // Switch active link states
        $('.active-link').removeClass('active-link');

        $('a[href="' + navTarget + '"]').addClass('active-link');


        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Galleries

        // Destroy all existing waypoints
        Waypoint.destroyAll();

        // Set up count for galleries to give them unique IDs
        let galleryCount = 0;

        // If there's a gallery
        $('.gallery').each(function () {

            // Get gallery element
            var $this = $(this);

            // Add ID via count
            galleryCount++;
            var thisId = 'gallery-' + galleryCount;
            $this.attr('id', thisId);

            // Gallery columns
            var galleryCols = $this.attr('data-columns');

            // Set up gallery container
            $this.append('<div class="gallery__wrap"></div>');

            // Add images to container
            $this.children('img').each(function () {
                $(this).appendTo('#' + thisId + ' .gallery__wrap');
            });

            // Wrap images
            $this.find('.gallery__wrap img').each(function () {
                var imageSrc = $(this).attr('src');
                $(this).wrapAll('<div class="gallery__item"><a href="' + imageSrc + '" class="gallery__item__link"></div></div>').appendTo();
            });

            // Wait for images to load
            $this.imagesLoaded(function () {

                // If it's a single column gallery
                if (galleryCols === '1') {

                    // Add carousel class to gallery
                    $this.addClass('gallery--carousel');

                    // Add owl styles to gallery wrap
                    $this.children('.gallery__wrap').addClass('owl-carousel');

                    // Use carousel
                    $this.children('.gallery__wrap').owlCarousel({
                        items: 1,
                        loop: true,
                        mouseDrag: false,
                        touchDrag: true,
                        pullDrag: false,
                        dots: true,
                        autoplay: false,
                        autoplayTimeout: 6000,
                        autoHeight: true,
                        animateOut: 'fadeOut'

                    });
                    // When scrolling over the bottom
                    let waypoint1 = new Waypoint({
                        element: document.getElementById(thisId),
                        handler: function (direction) {

                            if (direction === 'down') {

                                // console.log('pause');

                                // Pause this carousel
                                $this.children('.gallery__wrap').trigger('stop.owl.autoplay');
                            }

                            if (direction === 'up') {

                                // console.log('play');

                                // Play this carousel
                                $this.children('.gallery__wrap').trigger('play.owl.autoplay');
                            }
                        },
                        offset: '-100%'
                    });

                    // When scrolling over the top
                    let waypoint2 = new Waypoint({
                        element: document.getElementById(thisId),
                        handler: function (direction) {

                            if (direction === 'down') {

                                // console.log('play');

                                // Play this carousel
                                $this.children('.gallery__wrap').trigger('play.owl.autoplay');
                            }

                            if (direction === 'up') {

                                // console.log('pause');

                                // Pause this carousel
                                $this.children('.gallery__wrap').trigger('stop.owl.autoplay');
                            }
                        },
                        offset: '100%'
                    });

                } else {

                    $this.addClass('gallery--grid');

                    // Use masonry layout
                    $this.children('.gallery__wrap').masonry({
                        itemSelector: '.gallery__item',
                        transitionDuration: 0
                    });

                    // Init fluidbox
                    $this.find('.gallery__item__link').fluidbox({
                        loader: true
                    });

                }

                // Show gallery once initialized
                $this.addClass('gallery--on');
            });

        });

        $('.project__images').each(function () {
            let $this = $(this);
            $this.imagesLoaded(function () {
                $this.owlCarousel({
                    items: 1,
                    touchDrag: true,
                    dots: true,
                    autoHeight: true,
                    margin: 20,
                    autoplay: true,
                    rewind: true
                });
                $this.on('translated.owl.carousel', function (event) {
                    changeSubtitle(event);
                });
            });
        });

        function changeSubtitle(event) {
            console.log(event);
            let t = $(event.target).find('.owl-item.active a').first();
            console.log(t);
            let name = t.attr('data-book-name');
            let url = t.attr('data-book-url');
            console.log(name, url);
            let description = t.attr('data-book-description') + `<a href="${url}"
                                       class="project__link button--text --right"
                                       style="color: #4C60E6; --color-var: #4C60E6">Leer</a>`;

            $('#book-name').html(name);
            $('#book-description').html(description);
        }

        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Format bytes for string units
        function formatBytes(bytes) {
            const units = ['S', 'KS', 'MS', 'GS', 'TS', 'PS', 'ES', 'ZS', 'YS'];
            bytes = Math.max(bytes, 0);
            let pow = Math.floor((bytes ? Math.log(bytes) : 0) / Math.log(1000));
            pow = Math.min(pow, units.length - 1);
            bytes /= Math.pow(1000, pow);

            return Math.round(bytes * 100) / 100 + units[pow];
        }

        $(document).on('click', '#fund', function () {
            console.log('Llamado al boton #fund');
            const el = $(this);
            el.prop('disabled', true);
            let project_solaris = parseInt(el.attr('data-projectamount'));

            let formated_solaris = formatBytes(project_solaris);
            let project_id = el.attr('data-projectid');
            let fund_amount = parseInt($('#fund__amount').val());

            if (isNaN(fund_amount) || fund_amount <= 0) {
                alert("Solo aceptamos Solaris. ¿Comunicamos su transgresión al sindicato?")
                el.prop('disabled', false);
                return;
            }

            let total = project_solaris + fund_amount;
            let formated_total = formatBytes(total);

            const dom__solaris__per_project = $('#solaris__per__project');
            dom__solaris__per_project.html(formated_total);
            dom__solaris__per_project.parent().addClass('animate__pulse');
            setTimeout(function () {
                dom__solaris__per_project.parent().removeClass('animate__pulse');
            }, 1000);

            el.attr('data-projectamount', total);

            $.get(`/blog/project/${project_id}/fund/${fund_amount}/`, function(res){
                console.log(res);
                if (res.error === true){
                    alert("Ha ocurrido un error")
                    dom__solaris__per_project.html(formated_solaris);
                } else{
                    dom__solaris__per_project.html(formatBytes(res.total));
                    $('#fund').attr('data-projectamount', res.total);
                }
                el.prop('disabled', false);
            }).catch(function(err){
                console.log(err);
                alert("Ha ocurrido un error")
                dom__solaris__per_project.html(formated_solaris);
                el.prop('disabled', false);
            });

            console.log('project_solaris: ' + project_solaris);
            console.log('total: ' + total);
        })

        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Images

        $('.post__content p > img').each(function () {
            var thisP = $(this).parent('p');
            $(this).insertAfter(thisP);
            $(this).wrapAll('<div class="image-wrap"></div>');
            thisP.remove();
        });

        // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Videos

        // For each iframe
        $('.post__content iframe').each(function () {

            // If it's YouTube or Vimeo
            if ($(this).attr('src').indexOf('youtube') >= 0 || $(this).attr('src').indexOf('vimeo') >= 0) {

                var width = $(this).attr('width');
                var height = $(this).attr('height');
                var ratio = (height / width) * 100;

                // Wrap in video container
                $(this).wrapAll('<div class="video" style="padding-bottom:' + ratio + '%;"></div>');

            }

        });

    }

    // Run functions on load
    pageFunctions();


    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Menu

    $(document).on('click', '.js-menu-toggle', function () {

        // If already open
        if (body.hasClass('menu--open')) {
            body.removeClass('menu--open');
        }

        // If not open
        else {
            body.addClass('menu--open');
        }
    });

    $(document).on('click', '.menu__list__item__link', function () {

        // If menu is open when you click a link on mobile
        if ($('.menu').hasClass('menu--open')) {
            $('.menu').removeClass('menu--open');
        }
    });


    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Listing post click

    // Click anywhere on the post to go to the link
    $(document).on('click', '.post', function () {

        var targetPost = $(this).find('.post__title a').attr('href');

        if (body.hasClass('ajax-loading')) {

            // Change navTarget
            navTarget = targetPost;

            // Switch the URL via History
            History.pushState(null, docTitle, targetPost);
        } else {
            // Use the given link
            window.location = targetPost;
        }
    });


    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Contact Form

    // Override the submit event
    $(document).on('submit', '#contact-form', function (e) {

        // Clear previous classes
        $('.contact-form__item--error').removeClass('contact-form__item--error');

        // Get form elements
        var emailField = $('.contact-form__input[name="email"]');
        var nameField = $('.contact-form__input[name="name"]');
        var messageField = $('.contact-form__textarea[name="message"]');
        var gotchaField = $('.contact-form__gotcha');

        // Validate email
        if (emailField.val() === '') {
            emailField.closest('.contact-form__item').addClass('contact-form__item--error');
        }

        // Validate name
        if (nameField.val() === '') {
            nameField.closest('.contact-form__item').addClass('contact-form__item--error');
        }

        // Validate message
        if (messageField.val() === '') {
            messageField.closest('.contact-form__item').addClass('contact-form__item--error');
        }

        // If all fields are filled, except gotcha
        if (emailField.val() !== '' && nameField.val() !== '' && messageField.val() !== '' && gotchaField.val().length === 0) {

            // Submit the form!
        } else {

            // Stop submission
            e.preventDefault();
        }

    });


}(jQuery));
