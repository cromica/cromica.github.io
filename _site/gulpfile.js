//Source and target locations
var assetSource = './_site/assets';
var assetTarget = './_site/assets/dist';

//specify source files
var source = {
    css: [
        assetSource + '/plugins/font-linecons/linecons.css',
        assetSource + '/css/superslides.css',
        assetSource + '/css/owl.carousel.css',
        assetSource + '/plugins/magnific-popup/magnific-popup.css',
        assetSource + '/css/reset.css',
        assetSource + '/css/framework.css',
        assetSource + '/css/typography.css',
        assetSource + '/css/layout.css',
        assetSource + '/css/blog.css',
        assetSource + '/css/color/blue.css',
        assetSource + '/css/syntax.css'

    ],
    scripts: [
        './site/js/search.min.js',
        assetSource + '/plugins/jquery-fitvids/jquery.fitvids.min.js',
        assetSource + '/plugins/jquery-appear/jquery.appear.js',
        assetSource + '/plugins/superslides/dist/jquery.superslides.min.js',
        assetSource + '/plugins/jquery-owl-carousel/owl.carousel.min.js',
        assetSource + '/plugins/carouFredSel/jquery.carouFredSel-6.2.1-packed.js',
        assetSource + '/plugins/jquery-countTo/jquery.countTo.js',
        assetSource + '/plugins/magnific-popup/jquery.magnific-popup.min.js',
        assetSource + '/plugins/jquery.mb.YTPlayer.js',
        assetSource + '/js/scripts.js',
        assetSource + '/js/blog.search.js',
    ]
};

//load dependencies
var gulp = require('gulp'),
shell = require('gulp-shell'),
gutil = require('gulp-util'),
watch = require('gulp-watch'),
plumber = require('gulp-plumber'),
imagemin = require('gulp-imagemin'),
pngquant = require('imagemin-pngquant'),
jpegtran = require('imagemin-jpegtran'),
gifsicle = require('imagemin-gifsicle'),

//js components
minifyHtml = require("gulp-minify-html"),
concat = require("gulp-concat"),
uglify = require("gulp-uglify"),

//css component
minifyCSS = require('gulp-minify-css');

//build site for production
gulp.task('build-prod', shell.task('jekyll build --config=_config.yml,_config.prod.yml'));

gulp.task('css',['build-prod'], function () {
    gulp.src(source.css)
      .pipe(concat('style.css'))
      .pipe(minifyCSS())
      .pipe(gulp.dest(assetTarget));   
});

gulp.task('js',['build-prod'], function () {
     gulp.src(source.scripts)
        .pipe(uglify({ mangle: false })).on('error', gutil.log)
       .pipe(concat("app.js"))
       .pipe(gulp.dest(assetTarget));    
});

gulp.task('html',['build-prod'], function () {
    gulp.src("./_site/**/*.html")
         .pipe(minifyHtml()).pipe(gulp.dest('./_site'));
    
});

gulp.task('imgmin',['build-prod'], function () {
    gulp.src("./_site/assets/images/**/*.*")
         .pipe(imagemin({
            progressive:true,
            svgoPlugins:[{removeViewBox:false}],
            optimizationLevel:7,
            use:[pngquant()]
         })).pipe(gulp.dest('./_site/assets/images'));
    
});

gulp.task('minify',['build-prod','css', 'js','html','imgmin']);
