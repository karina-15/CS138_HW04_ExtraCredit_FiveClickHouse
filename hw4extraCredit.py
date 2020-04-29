#! /usr/bin/python
# Homework No.  04
# Extra Credit
# File Name:    hw4extraCredit.py
# Programmer:   Karina Elias
# Date:         Sep. 15, 2019
#
# Problem Statement: Programming Exercise #11 p.120
# Five-click house
# This program allows the user to draw a simple
# house using 5 mouse-clicks. First 2 clicks draw
# the opposite corners of the rectangular base. The
# 3rd click will be the middle of the top edge of
# the rectangular door. The door width is 1/5th the
# width of the house frame. The 4th click is the
# center of a square window which is 1/2 the width
# of the door width. The last click is the peak of
# the triangular roof.
#
#
# Overall Plan:
# 1. Create graphics window
# 2. Print introduction
# 3. Prompt user for 1st click (1 corner of base)
# 4. Prompt user for 2nd click (2nd corner of base)
# 5. Draw the rectangular base
# 6. Prompt user for 3rd click (middle pt of door's
#    top edge)
# 7. Draw rectangular door 1/5th width of base
# 8. Prompt user for 4th click (center of window)
# 9. Draw square window 1/2 the door width
# 10. Prompt user for last (5th) click (roof peak)
# 11. Click to close window
#
#
# import the necessary python libraries
from graphics import *  # import everything defined in graphics.py


def main():
    # Create graphics window
    win = GraphWin("Five-click house", 500, 500)
    win.setBackground("#333333")  # Dark grey window background

    # Print introduction
    intro = Text(Point(250, 15), "This program allows you to draw a house")
    intro.setTextColor("#FFFFFF")
    intro.draw(win)

    # ---Window Layout--- #

    # Create white rectangle for house drawing area
    house_canvas = Rectangle(Point(5, 30), Point(498, 470))
    house_canvas.setFill("#FFFFFF")
    house_canvas.draw(win)

    # Display label at bottom of window for user prompt and information
    info_label = Text(Point(250, 485), "1. Click in the white box to draw"
                                       " the 1st corner of the house base.")
    info_label.setTextColor("#FFFFFF")
    info_label.draw(win)

    # ---Input--- #
    # Get user click point and draw the 1st corner
    base_corner = win.getMouse()
    base_x1 = base_corner.getX()
    base_y1 = base_corner.getY()
    base_corner_pt = Point(base_x1, base_y1)
    base_corner_pt.draw(win)

    # Update prompt at bottom of window
    info_label.setText("2. Click again to draw the opposite corner"
                       " of the house base")

    # Get user click point for opposite corner of base
    base_opp_corner = win.getMouse()
    base_x2 = base_opp_corner.getX()
    base_y2 = base_opp_corner.getY()
    base_opp_corner_pt = Point(base_x2, base_y2)

    # ---Process--- #
    # Draw the rectangular base
    rect_base = Rectangle(base_corner_pt, base_opp_corner_pt)
    rect_base.setWidth(2)
    rect_base.draw(win)

    # Update prompt at bottom of window
    info_label.setText("3. Click inside the house base to draw"
                       " the top edge of the door")

    # Get user click point for door's top edge
    # and calculate door's rectangle opposite corner pts
    door_top_middle_pt = win.getMouse()
    door_top_middle_x = door_top_middle_pt.getX()
    base_width = base_x2 - base_x1
    # 1/5th of base & 1/2 b/c it is the middle pt & need to get corner pt
    door_tl_corner_x_pt = door_top_middle_x - (base_width / (5 * 2))
    door_br_corner_x_pt = door_top_middle_x + (base_width / (5 * 2))
    door_tl_corner_y_pt = door_top_middle_pt.getY()
    if base_y1 > base_y2:
        door_br_corner_y_pt = base_y1
    else:
        door_br_corner_y_pt = base_y2

    # Draw door
    rect_door = Rectangle(Point(door_tl_corner_x_pt, door_tl_corner_y_pt),
                          Point(door_br_corner_x_pt, door_br_corner_y_pt))
    rect_door.setWidth(2)
    rect_door.draw(win)

    # Update prompt at bottom of window
    info_label.setText("4. Click inside the house base to draw"
                       " the window")

    # Get user click point for the windows center point
    # and calculate window's opposite corner points
    window_center_pt = win.getMouse()
    window_center_x = window_center_pt.getX()
    window_center_y = window_center_pt.getY()
    door_width = door_br_corner_x_pt - door_tl_corner_x_pt
    # 1/2 of door width & 1/2 for center to corner pt
    distance_window_center_corner = door_width / (2 * 2)
    window_tl_corner_x_pt = window_center_x - distance_window_center_corner
    window_br_corner_x_pt = window_center_x + distance_window_center_corner
    window_tl_corner_y_pt = window_center_y - distance_window_center_corner
    window_br_corner_y_pt = window_center_y + distance_window_center_corner

    # Draw window
    rect_window = Rectangle(
        Point(window_tl_corner_x_pt, window_tl_corner_y_pt),
        Point(window_br_corner_x_pt, window_br_corner_y_pt))
    rect_window.setWidth(2)
    rect_window.draw(win)

    # Update prompt at bottom of window
    info_label.setText("5. Click above the house base to draw"
                       " the roof")

    # Get user click point for roof's peak
    roof_peak_pt = win.getMouse()

    # ---Output--- #

    # Draw roof
    if base_y1 < base_y2:
        triangle_roof = Polygon(Point(roof_peak_pt.getX(), roof_peak_pt.getY()),
                                Point(base_x1, base_y1),
                                Point(base_x2, base_y1))
    else:
        triangle_roof = Polygon(Point(roof_peak_pt.getX(), roof_peak_pt.getY()),
                                Point(base_x1, base_y2),
                                Point(base_x2, base_y2))
    triangle_roof.setWidth(2)
    triangle_roof.draw(win)

    # Close window
    info_label.setText("Click to exit")
    win.getMouse()  # pause for click in window
    win.close()


main()
