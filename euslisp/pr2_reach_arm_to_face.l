#!/usr/bin/env roseus
(load "package://pr2eus/pr2-interface.l")
(ros::load-ros-manifest "face_detector_mono")

(setq *denom-x* 25)
(setq *denom-y* (/ (* *denom-x* 480) 640))

(ros::roseus "pr2_reach_arm_to_face")

(pr2-init)
(if (not (boundp '*irtviewer*)) (make-irtviewer))
(objects (list *pr2*))

(defun extend-rarm()
  (send *pr2* :rarm :collar-y :joint-angle 0)
  (send *pr2* :rarm :shoulder-r :joint-angle 0)
  (send *pr2* :rarm :shoulder-p :joint-angle 0)
  (send *pr2* :rarm :elbow-p :joint-angle -10)
  (send *ri* :angle-vector (send *pr2* :angle-vector) 3000)
  (send *ri* :wait-interpolation)
  )

(defun callback (msg)
  (setq *msg* msg)
  (if (not (send msg :rects)) (return-from callback nil))
  (let* ((rect (car (send msg :rects)))
         (x (send rect :x))
         (y (send rect :y))
         (height (send rect :height))
         (width  (send rect :width))
         (center-x (+ x (/ width 2)))
         (center-y (+ y (/ height 2))))
    
    (send *pr2* :rarm :collar-y :joint-angle (- (/ center-x *denom-x*)))
    (send *pr2* :rarm :shoulder-p :joint-angle (/ center-y *denom-y*))
    (send *ri* :angle-vector (send *pr2* :angle-vector) 1000)
    (if (boundp '*irtviewer*) (send *irtviewer* :draw-objects))
    (send *ri* :wait-interpolation)
    )
  )

(ros::subscribe "/face_detector_mono/faces" face_detector_mono::RectArray #'callback) 

(warn "(main)")
(defun main ()
  (extend-rarm)
  (ros::rate 10)
  (while (ros::ok)
         (ros::spin-once)
         (ros::sleep)
         )
  )









;; ************************
;; actionlib ver... not implemented yet
;;
;;(ros::load-ros-manifest "agentsystem")
;;(ros::load-ros-manifest "actionlib")
;;(ros::load-ros-manifest "pr2_controller_msgs")

;;(setq *r-arm-client* (instance ros::simple-action-client
;;                               :init "pr2_controller_msgs/JointTrajectoryAction"
;;                               pr2_controller_msgs::JointTrajectoryAction))

;;(defun callback (msg)
;;  (let ((x (send (send msg :data) :x))
;;        (y (send (send msg :data) :y)))
;;    (send *r-arm-client* : )
;;    (send *r-arm-client* :header :stamp (ros::time+ (ros::time-now) (ros::time 10)))
;;
;;    )
;;  )


;; % rosmsg show face_detector_mono/RectArray
;; std_msgs/Header header
;;   uint32 seq
;;   time stamp
;;   string frame_id
;; face_detector_mono/Rect[] rects
;;   int32 x
;;   int32 y
;;   int32 width
;;   int32 heigh

