/**
 *
 * Version : $Id$
 * This file was generated by Aldebaran Robotics ModuleGenerator
 */

#include "onmarkdetection.h"

#include <alvalue/alvalue.h>
#include <alcommon/alproxy.h>
#include <alcommon/albroker.h>
#include <althread/alcriticalsection.h>

#include <qi/log.hpp>


OnMarkDetection::OnMarkDetection(
  boost::shared_ptr<AL::ALBroker> broker,
  const std::string& name):
    AL::ALModule(broker, name),
    fMemoryProxy(getParentBroker()),
    fFaces(AL::ALValue()),
    fFacesCount(0),
    fCallbackMutex(AL::ALMutex::createALMutex())
{
  setModuleDescription("This is an autogenerated module, this descriptio needs to be updated.");

  functionName("callback", getName(), "");
  BIND_METHOD(OnMarkDetection::callback);

}

OnMarkDetection::~OnMarkDetection() {}

void OnMarkDetection::init() {
  try {
    /** See if there is any face already detected at initialization. */
    fFaces = fMemoryProxy.getData("LandmarkDetected");
    if (fFaces.getSize() < 2) {
      qiLogInfo("module.example") << "No face detected." << std::endl;
      fTtsProxy.say("No face detected");
    } else {
      qiLogInfo("module.example") << "Face detected." << std::endl;
      fTtsProxy.say("Face detected");
    }
    /** Subscribe to the event LandmarkDetected, with appropriate callback function. */
    fMemoryProxy.subscribeToEvent("LandmarkDetected", "OnMarkDetection", "callback");
  }
  catch (const AL::ALError& e) {
    qiLogError("module.name") << e.what() << std::endl;
  }
}

void OnMarkDetection::callback() {
  /** Use a mutex to make it all thread safe. */
  AL::ALCriticalSection section(fCallbackMutex);
  try {
    /** Retrieve the data raised by the event. */
    fFaces = fMemoryProxy.getData("LandmarkDetected");
qiLogInfo("module.name") <<fFaces<<std::endl;
    /** Check that there are faces effectively detected. */
    if (fFaces.getSize() < 2 ) {
      if (fFacesCount != 0) {
        qiLogInfo("module.example") << "No face detected." << std::endl;
        fTtsProxy.say("No face detected.");
        fFacesCount = 0;
      }
	fTtsProxy.say("1 face.");
      return;
    }
    /** Check the number of faces from the FaceInfo field, and check that it has
    * changed from the last event.*/
    if (fFaces[1].getSize() - 1 != fFacesCount) {
      qiLogInfo("module.name") << fFaces[1].getSize() - 1 << " face(s) detected." << std::endl;
      char buffer[50];
      sprintf(buffer, "%d faces detected.", fFaces[1].getSize() - 1);
      fTtsProxy.say(std::string(buffer));
      /** Update the current number of detected faces. */
      fFacesCount = fFaces[1].getSize() - 1;
    }
  }
  catch (const AL::ALError& e) {
    qiLogError("module.name") << e.what() << std::endl;
  }
}
