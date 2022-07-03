<div class="row">                
                    <div class="col-xl-7">
                        <div class="ibox">
                            <div class="ibox-head">
                                <div class="ibox-title">Sales Processing</div>
                            </div>
                            <div class="ibox-body">
                                <form class="form-horizontal" method="POST" action="">
                                    {% csrf_token %}
                                    <div class="form-group row">
                                        <label class="col-sm-4 col-form-label">Receipt Type</label>
                                        <div class="col-sm-8">
                                           {{form.receipt_types}}
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <label class="col-sm-4 col-form-label">Receipt No</label>
                                        <div class="col-sm-8">
                                           {{form.receipt_no}}
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                            <label class="col-sm-4 col-form-label">Receipt Print</label>
                                            <div class="col-sm-8">
                                              <select class="form-control" name="autoprint">
                                              {% for item in autoprint %}
                                                <option value={{item.id }} {% if item.id == autoFormPrint.status.id %} selected {% endif %}> {{item.title}} </option>

                                                {% endfor %}
                                            </select>
                                            </div>
                                        </div>
                                
                                    <div class="form-group row">
                                        <div class="col-sm-8 ml-sm-auto">
                                             {% if button_show %}
                                                <button class="btn btn-info" type="submit" name='btn-process'>Submit</button>
                                            {% endif %}
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div> 