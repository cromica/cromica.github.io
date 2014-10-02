
desc "Delete _site"
task :delete do 
 puts "\## Deleting _site/"
 status = system("rd /s /q _site")
 puts status ? "Succes": "Failed"
end

desc "Preview _site/"
task :preview do
  puts "\n## Opening _site/ in browser"
  # status = system("open http://0.0.0.0:4000/")
  # puts status ? "Success" : "Failed"
  output = system("dir")
  $?
  p output

end


desc "Build _site/ for development"
  task :dev do
    puts "\n##  Starting Sass and Jekyll"
    pids = [spawn("jekyll serve -w")]

    trap "INT" do
      Process.kill "INT", *pids
      exit 1
    end

    loop do
      sleep 1
    end
  end
 
 desc "Build _site/ for production"
  task :build do
    puts "\n## Building Jekyll to _site/"
    status = system("jekyll build")
    puts status ? "Success" : "Failed"
    Rake::Task["minify"].invoke
  end

  desc "Commit _site/"
task :commit do
  puts "\n## Staging modified files"
  status = system("git add -A")
  puts status ? "Success" : "Failed"
  puts "\n## Committing a site build at #{Time.now.utc}"
  message = "Build site at #{Time.now.utc}"
  status = system("git commit -m \"#{message}\"")
  puts status ? "Success" : "Failed"
  puts "\n## Pushing commits to remote"
  status = system("git push origin source")
  puts status ? "Success" : "Failed"
end