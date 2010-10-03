cdef extern from "Python.h":
    ctypedef unsigned short Py_UNICODE

cdef extern from "JavaScriptCore/JSStringRef.h":
    ctypedef Py_UNICODE JSChar
    void JSStringRelease(JSStringRef string)
    JSStringRef JSStringCreateWithUTF8CString(char* string)
    JSStringRef JSStringCreateWithCharacters(JSChar* chars, size_t numChars)
    size_t JSStringGetLength(JSStringRef string)
    JSChar* JSStringGetCharactersPtr(JSStringRef string)
    size_t JSStringGetMaximumUTF8CStringSize(JSStringRef string)
    size_t JSStringGetUTF8CString(JSStringRef string, char* buffer, size_t bufferSize)
