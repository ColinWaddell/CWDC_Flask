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
                    src : [
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
                command: '/bin/bash -c "source env/bin/activate && python index.py"',
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

    // define default task
    grunt.registerTask('default', ['shell:flaskRun', 'browserSync', 'watch']);
};
