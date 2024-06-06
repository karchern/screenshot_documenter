# screenshot_documenter

Simple program that can be used to capture and store an arbitrary number of screenshots to ultimately save them
to a powerpoint.

Works only on macOS, probably (requires the `screencapture` CL tool that afaik only exists on macOS?)

# installation

`conda create -n documenter`
`pip install -e .`

# usage

From a terminal, `cd` to the location of the git repo and run `python -m documenter`. Take screenshots by pressing `shift + cmd` to designate the first corner and by left clicking to designate the second corner of the screenshot rectangle.
This cycle can be repeated ad nauseam. Press `esc` to write the file to a `.pptx`.
