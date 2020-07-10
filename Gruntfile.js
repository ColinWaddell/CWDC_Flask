var staticPathPrefix = 'static',
    proxyUrl = 'localhost:5000';

module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            files: staticPathPrefix + '/sass/**/*.{scss,sass}',
            tasks: ['sass']
        },
        sass: {
            dev: {
                files: [{
                    expand: true,
                    cwd: staticPathPrefix + '/sass',
                    src: ['*.scss', '*.sass'],
                    dest: staticPathPrefix + '/css',
                    ext: '.css'
                }]
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src: [
                        staticPathPrefix + '/css/*.css',
                        staticPathPrefix + '/js/*.js',
                        'templates/*.html',
                        'content/*.md',
                        '**/*.py'
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: proxyUrl,
                    online: true
                }
            }
        },
        shell: {
            flaskRun: {
                command: 'env/bin/python index.py',
                options: {
                    stdout: true,
                    failOnError: true,
                    async: true
                }
            },
            flaskRunWindows: {
                command: 'env\\Scripts\\python.exe index.py',
                options: {
                    stdout: true,
                    failOnError: true,
                    async: true
                }
            }
        }
    });

    // load npm tasks
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-shell-spawn');

    // define development tasks
    grunt.registerTask('default', ['shell:flaskRun', 'browserSync', 'watch']);
    grunt.registerTask('windows', ['shell:flaskRunWindows', 'browserSync', 'watch']);
};
