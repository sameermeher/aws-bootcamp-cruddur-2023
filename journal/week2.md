# Week 2 — Distributed Tracing

## Homework Challenges
**This is best week in terms of learning lot of new tools and trying out** 
1. **Distributing Tracing** - 
   - Honeycomb - Spans and ability to capture custom attributes and build a Dashboard for observability
   - X-Ray - Instrumenting with X-Ray and able to create sub-segments with metadata and annotations
2. **Error Tracing** - 
   - Rollbar - Ability to capture errors occuring in the application.
3. **CloudWatch Logs** -
   - Logging details of what's happening in the application  


Details of Homework and Tasks attempted this week -   
1. **HONEYCOMB - Instrumentation to adding more custom attributes**  
    This was a new tool for me but found it most convinient tool w.r.t. Distributed Tracing. It's dead simple :)

    Created Spans and multiple sub-spans to trace the route of a request. Example below is with creation of 2 spans-
    ![Spans](../_docs/assets/week-2/honeycomb/1-spans.png)
    Recent Traces captured -
    ![Multiple Spans](../_docs/assets/week-2/honeycomb/2-multiple-spans.png)

    For adding extra spans with custom attributes, I selected "Create Activity" action wherein, logged-in User could add posts which intiates "Create Activity" action/api in the background.
    ```
    now = datetime.now(timezone.utc).astimezone()
    # Adding a extra attributes to current span
    span = trace.get_current_span()
    span.set_attribute("app.now", now.isoformat())

    span.set_attribute("app.user_handle", user_handle)

    ```
    ![Traces for Create Activity](../_docs/assets/week-2/honeycomb/4-trace-for-create-activity.png)

    ![Custome Attributes](../_docs/assets/week-2/honeycomb/3-trace-with-custom-attributes.png)

    In addition to creating and saving the query, there as a option to create a Dashboard and add query into it for better observability.
    As we don't have database integration as of now I intentionally added delay with sleep command (while Creating Activity in create_activity.py file)
    ```
    # Generate a random sleep time between 50 and 500 milliseconds to replicate delay scenario
    sleep_time = random.randint(50, 500) / 1000
    time.sleep(sleep_time)
    ```
    ![Dashboard with Observability](../_docs/assets/week-2/honeycomb/5-dashboard-monitor-observability.png)
    ![Query for Latency Tracking](../_docs/assets/week-2/honeycomb/6-query-latency-by-user-handle.png)

2. **X-RAY - Instrumentation to adding subsegments with metadata and annotations**  

    Wrapped the block for sub-segment instrumentation -
    ![Explicit Delay in Code](../_docs/assets/week-2/x-ray/0-delay-added-in-code-sleep.png)
    Generated traces -
    ![Trackes](../_docs/assets/week-2/x-ray/1-traces.png)
    Able to use subsegment by adding metadata and annotations (which could be useful to write to query against it)
    ![Subsegments with Metadata](../_docs/assets/week-2/x-ray/2-traces-subsegment-with-metadata-annotations.png)

3. **CLOUDWATCH Logs**  
    Added logs in the code to be captured in CloudWatch logs.
    ![Log Streams](../_docs/assets/week-2/cloudwatch-logs/1-log-streams.png)

    ![Logs](../_docs/assets/week-2/cloudwatch-logs/2-logs.png)

4. **ROLLBAR - Error Tracking**  
    For Rollbar I experimented for real time scenarios with issues while invoking API becuause of wrong input or missing input and ability to capture those errors in Rollbar.
    Here is the screenshot from the codebase and then from rollbar where I could capture those scenarios.
    ![Code - Report Error](../_docs/assets/week-2/rollbar/1-rollbar-reporterrors.png)

    ![Errors Tracked](../_docs/assets/week-2/rollbar/2-error-tracked-in-rollbar.png)